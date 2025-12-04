# main make extract French and English notebooks and package them into a tar.gz file
# They are also visible in notebooks/fr and notebooks/en
#
system/notebooks_cama.tgz:
	mkdir -p notebooks/fr notebooks/en
	cd notebooks; make traduction
	rm -f system/notebooks_cama.tgz
	tar --transform 's|^notebooks|cama|' -czvf system/notebooks_cama.tgz notebooks/fr notebooks/en notebooks/.jupyter 

clean:
	rm -f system/notebooks_cama.tgz cama_html_fr.tgz cama_html_en.tgz
	rm -rf notebooks/fr notebooks/en

# To create English and French HTML versions of the notebooks
#
html: system/notebooks_cama.tgz
	# french
	tar xvf system/notebooks_cama.tgz
	mv "cama/fr/_Table des matières.ipynb" "cama/fr/Table des matières.ipynb"
	echo "-> HTML"
	uv run system/ipynb2html.py cama/fr cama_fr 
	echo "-> HTML done"
	cp -r "cama/fr/images" "cama_fr/"
	sed -i -e 's/ipynb/html/g' cama_fr/Table\ des\ matières.html
	tar czvf cama_html_fr.tgz cama_fr
	# english
	mv "cama/en/_Table of contents.ipynb" "cama/en/Table of contents.ipynb"
	uv run system/ipynb2html.py cama/en cama_en 
	cp -r "cama/fr/images" "cama_en/"
	sed -i -e 's/ipynb/html/g' cama_en/Table\ of\ contents.html
	tar czvf cama_html_en.tgz cama_en
	# clean
	rm -rf cama
	rm -rf cama_fr
	rm -rf cama_en


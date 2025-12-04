traduction:
	rm -rf fr en
	mkdir en
	mkdir fr
	cp -r images fr/
	cp -r data fr/
	cd en; ln -s ../fr/images .
	cd en; ln -s ../fr/data .
	./extract_lang.py *.ipynb
	cd fr; uv run ../make_toc.py
	cd en; uv run ../make_toc.py

import json
import os
import re
import ipykernel
import requests
from notebook.notebookapp import list_running_servers
from urllib.parse import urljoin
from IPython.display import display, Markdown

def get_notebook_path():
    """
    Return the full path of the jupyter notebook.
    """
    session = requests.Session()
    session.trust_env = False
    kernel_id = re.search('kernel-(.*).json',
                          ipykernel.connect.get_connection_file()).group(1)
    servers = list_running_servers()
    if 
    for ss in servers:
        response = session.get(f"{ss['url']}api/sessions",
                               params={'token': ss['token']})
        for nn in json.loads(response.text):
            if nn['kernel']['id'] == kernel_id:
                try:
                    return os.envion['HOME_URL'] + 'notebooks/' + nn['notebook']['path']
                except:
                    return ss['url'] + 'notebooks/' + nn['notebook']['path']

def PreviousNext(url1, url2):
    section = get_notebook_path()
    section = section.replace('notebooks','tree')
    section = section[:section.rfind('/')]
    toc = "http://python3.mooc.lrde.epita.fr/notebooks/Table%20des%20mati%C3%A8res.ipynb"
    text = 200 * "&nbsp; "
    text += "<br/><center>"
    text += f'<a href="{url1}">{url1[url1.rfind("/")+1:-6]}</a>'
#    text += f'&nbsp; ← <a href="{section}" style="text-decoration:none"> △ </a> → &nbsp;'
    text += f'&nbsp; ← <a href="{toc}" style="text-decoration:none"> △ </a> → &nbsp;'
    text += f'<a href="{url2}">{url2[url2.rfind("/")+1:-6]}</a>'
    text += '</center><br/>'
    text += '&nbsp;'
    return text


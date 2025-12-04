#! /usr/bin/env python3

import os
import sys
import re
import nbformat
import glob

if os.getcwd().split('/')[-1] == "fr":
    f0 = "_Table des matières.ipynb"
else:
    f0 = "_Table of contents.ipynb"

sys.stdout = open(f0, 'w')

print('''
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
''')
print(f'"## {f0[1:]}\\n",')
files = sorted(glob.glob("*.ipynb"))
if files[0] == f0:
    files = files[1:]
for notebook in files:
    levels = set()
    previous_level = 0
    with open(notebook, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

        print('"* [%s](%s)\\n",' % (notebook[:-6], 
                                    notebook.replace(' ','%20')))
        level_prev = 1  # je viens de faire un <ul>
        for cell in nb.cells:
            if cell["cell_type"] == "markdown":
                    for line in cell['source'].split('\n'):
                        try:
                            if re.search('^[ ]*#+', line) != None:
                                line = line.split("\n")[0]
                                line = re.sub('^[ ]*','',line)
                                line = re.sub(r'\\',r'\\\\',line)
                                line = re.sub('"','\\\\"',line)
                                level = len(line.split(' ')[0])
                                if level < 4:
                                    if level > previous_level:
                                        levels.add(level)
                                    elif level < previous_level:
                                        levels.remove(previous_level)
                                    previous_level = level
                                    print('"%s\\n",' % re.sub('[#]+',
                                                              len(levels)*'    '+'-  ',
                                                              line))
    #                            level = len(line.split(' ')[0])
    #                            if level > level_prev:
    #                                print((level - level_prev)*"<ul>")
    #                            else:
    #                                print((level_prev - level)*"</ul>")
    #                            level_prev = level
    #                            print(re.sub('^[#]{%d} (.*)' % level,
    #                                         '<li> \\1 </li>',
    #                                         line))
                        except:
                            pass
print('''
    ""
 ]}],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
''')

sys.stdout.close()

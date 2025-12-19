## Web

This course is visible online / ce cours est en ligne :

https://www.ricou.eu.org/cama_fr/Table%20des%20mati%C3%A8res.html
https://www.ricou.eu.org/cama_en/Table%20of%20contents.html

## Make

This course is in French and English. Notebooks are in both languages.
`make` produces `notebooks/fr/` and `notebooks/en/` with their respective
language. You should always modify the notebooks in `notebooks` and
be sure to have the right tag for the language if you add new cells
(check in source code).

Ce cours est en français et anglais. Les notebooks sont dans les 2 langues.

Un simple `make` va découper les fichiers dans `notebooks` en `notebooks/fr/`
et `notebooks/en/`. On peut faire la même chose avec `make traduction` dans
le répertoire `notebooks`.

Si vous modifiez les notebooks, faite le sur ceux de `notebooks` sinon
un make va écraser vos modifications dans les sous-répertoire en et fr.
Si vous ajoutez des cellules, il faut indiquer la langue de la cellule
ce que je fais directement dans le code source.

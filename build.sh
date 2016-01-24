#!/bin/bash

sphinx-intl update -p _build/locale -l de
sphinx-intl build

rm -r deploy
mkdir -p deploy

cp index.html.* deploy

make -e SPHINXOPTS="-D language='de'" html
mv _build/html deploy/de

make -e SPHINXOPTS="-D language='en'" html
mv _build/html deploy/en

scp -r deploy/* rasp:portfolio
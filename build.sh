#!/bin/bash

make gettext
sphinx-intl update -p _build/locale -l de
sphinx-intl build

convert img/favicon.svg -resize 256x256 -define icon:auto-resize="256,128,96,64,48,32,16" img/favicon.ico

rm -r deploy
mkdir -p deploy

cp index.html.* deploy
cp BingSiteAuth.xml googlee1eadb2ddedaa639.html sitemap.* deploy

make -e SPHINXOPTS="-D language='de'" html
mv _build/html deploy/de

make -e SPHINXOPTS="-D language='en'" html
mv _build/html deploy/en

cp img/portrait.jpg img/cc.png deploy/de/_images
cp img/portrait.jpg img/cc.png deploy/en/_images

scp -r deploy/* rasp:portfolio

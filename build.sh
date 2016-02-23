#!/bin/bash

make gettext
sphinx-intl update -p _build/locale -l de
sphinx-intl build

rm favicon.{png,ico}
convert  -background none img/logo.svg -resize 256x256 img/favicon.png
convert img/favicon.png -define icon:auto-resize="256,128,96,64,48,32,16" img/favicon.ico

rm -r deploy
mkdir -p deploy

cp index.html.* img/favicon.ico img/logo.svg img/loading.gif deploy
cp BingSiteAuth.xml googlee1eadb2ddedaa639.html sitemap.* robots.txt deploy

make -e SPHINXOPTS="-D language='de'" html
mv _build/html/* deploy/
mkdir deploy/de
mkdir deploy/en
mv deploy/*.{html,js} deploy/de

make -e SPHINXOPTS="-D language='en'" html
mv _build/html/*.{html,js} deploy/en

sed -i "s|_|../_|g" deploy/{de,en}/*.html
sed -i "s|<script |<script async |g" deploy/{de,en}/*.html

cp img/portrait.jpg img/cc.png deploy/_images

scp -r deploy/* rasp:portfolio

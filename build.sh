#!/bin/bash

convert -background none content/img/logo.svg -resize 256x256 content/extra/favicon.png
convert content/extra/favicon.png -define icon:auto-resize="256,128,96,64,48,32,16" content/extra/favicon.ico

DEBUG=1 make publish

# fix for gh pages
touch output/.nojekyll

echo "copy to deploy"
cp -r output deploy

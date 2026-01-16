#!/usr/bin/bash

fortune | cowsay -f dragon

git add .
git commit -m "$1"
git push origin "$2"
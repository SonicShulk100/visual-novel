#!/usr/bin/bash

cowsay -f dragon "Time to commit motherfucker!"

git add .
git commit -m "$1"
git push origin "$2"
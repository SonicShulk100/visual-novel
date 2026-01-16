#!/usr/bin/bash

git switch "$1"

git pull

git rebase "origin/$2"

git push -u origin "$1"
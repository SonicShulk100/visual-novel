#!usr/bin/env sh

#==================================
# Fetching and pulling the project.
#==================================
git fetch && git pull

#==================
# Switching to Main
#==================

git switch main && git pull && git rebase origin/main && git push -u origin main


#==============
# Main branches
#==============

#=====================
# Switching to script
#=====================

git switch script && git pull && git rebase origin/main && git push -u origin script

#====================
# Switching to images
#====================

git switch images && git pull && git rebase origin/main && git push -u origin images

#===================
# Switching to audio
#===================

git switch audio && git pull && git rebase origin/main && git push -u origin audio

#=======================
# Switching back to Main
#=======================

git switch main && git pull

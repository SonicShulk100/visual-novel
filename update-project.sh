#!/usr/bin/bash

git fetch origin

git switch main && git pull && git rebase origin/main && git push -u origin main

#==============
# Main Branches
#==============
MAIN_BRANCHES=("script" "images" "audio" "gui")

for MAIN_BRANCH in "${MAIN_BRANCHES[@]}"; do
  git switch "$MAIN_BRANCH"
  git pull
  git rebase origin/main
  git push -u origin "$MAIN_BRANCH"
done

#======================
# Sub Branches : SCRIPT
#======================
SCRIPT_BRANCHES=("script-characters" "script-narration" "script-choices")

for SUB_SCRIPT_BRANCH in "${SCRIPT_BRANCHES[@]}"; do
  git switch "$SUB_SCRIPT_BRANCH"
  git pull
  git rebase origin/main
  git push -u origin "$SUB_SCRIPT_BRANCH"
done


#=====================
# Sub Branches : IMAGE
#=====================
IMAGE_BRANCHES=("images-characters" "images-backgrounds")

for SUB_IMAGE_BRANCH in "${IMAGE_BRANCHES[@]}"; do
  git switch "$SUB_IMAGE_BRANCH"
  git pull
  git rebase origin/main
  git push -u origin "$SUB_IMAGE_BRANCH"
done


#=====================
# Sub Branches : AUDIO
#=====================
AUDIO_BRANCHES=("audio-sfx" "audio-music")

for SUB_AUDIO_BRANCH in "${AUDIO_BRANCHES[@]}"; do
  git switch "$SUB_AUDIO_BRANCH"
  git pull
  git rebase origin/main
  git push -u origin "$SUB_AUDIO_BRANCH"
done

git switch main && git pull

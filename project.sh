#!/usr/bin/bash

set -e

read -p "Enter the command : " command

case $command in 
    (commit)
        read -p "Enter the commit message : " commitMessage
        read -p "Enter the branch you're in : " commitBranch
        {
            if [[ -z "$commitMessage" || -z "$commitBranch" ]]; then
                cowsay -d "Enter either the message or the branch"
                exit 1
            fi

            git add .
            git commit -m "$commitMessage"
            git push -u origin "$commitBranch"

            cowsay -g "Commiting complete."
        } || {
            cowsay -d "Something went wrong...!"
            exit 1
        }
        ;;
    (rebase)
        read -p "Enter the source branch : " sourceBranch
        read -p "Enter the target branch : " targetBranch
        {
            if [[ -z "$sourceBranch" || -z "$targetBranch" ]]; then
                cowsay -d "Enter either the message or the branch."
                exit 1
            fi
            git fetch origin
            git switch "$targetBranch"
            git pull
            git rebase origin/"$sourceBranch"
            git push -u origin "$targetBranch"

            cowsay -g "Rebasing complete."
        } || {
            cowsay -d "Something went wrong...!"
            exit 1
        }
        ;;
    (update)
        {
            git fetch origin
            
            git switch main
            git pull

            #==============
            # Main Branches
            #==============

            MAIN_BRANCHES=("gui" "script" "audio" "images")
            for MAIN_BRANCH in "${MAIN_BRANCHES[@]}"; do
                git switch "$MAIN_BRANCH"
                git pull
                git rebase origin/main
                git push -u origin "$MAIN_BRANCH"
            done

            #======================
            # Sub-Branches : Script
            #======================
            BRANCHES_SCRIPT=("script-characters" "script-choices" "script-narration")
            for BRANCH_SCRIPT in "${BRANCHES_SCRIPT[@]}"; do
                git switch "$BRANCH_SCRIPT"
                git pull
                git rebase origin/main
                git push -u origin "$BRANCH_SCRIPT"
            done

            #=====================
            # Sub-Branches: Images
            #=====================
            BRANCHES_IMAGES=("images-backgrounds" "images-characters")
            for BRANCH_IMAGE in "${BRANCHES_IMAGES[@]}"; do
                git switch "$BRANCH_IMAGE"
                git pull
                git rebase origin/main
                git push -u origin "$BRANCH_IMAGE"
            done

            #====================
            # Sub-Branches: Audio
            #====================
            BRANCHES_AUDIO=("audio-music" "audio-sfx")
            for BRANCH_AUDIO in "${BRANCHES_AUDIO[@]}"; do
                git switch "$BRANCH_AUDIO"
                git pull
                git rebase origin/main
                git push -u origin "$BRANCH_AUDIO"
            done

            git switch main
            git pull

            cowsay -g "Updating complete."
        } || {
            cowsay -d "Something went wrong...!"
            exit 1
        }
        ;;
esac

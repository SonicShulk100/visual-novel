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
esac

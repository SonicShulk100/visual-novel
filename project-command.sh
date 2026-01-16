#!/usr/bin/bash

set -e

read -p "Enter the command: " command

case $command in 
    (commit)
        read -p "Enter the commit -message : " comment
        read -p "Enter the branch you're in : " branch

        {
            git add .
            git commit -m "$comment"
            git push -u origin "$branch"
        } || {
            echo "An error occurred during the git operations."
        }
        ;;
    (rebase)
        read -p "Enter the source branch : " sourceBranch
        read -p "Enter the target branch : " targetBranch
        {
            git switch "$targetBranch"
            git pull
            git rebase origin/"$sourceBranch"
            git push -f origin "$targetBranch"
        } ||
        {
            echo "An error occurred during the git rebase operation."
        }
        ;;
esac
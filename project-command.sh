#!/usr/bin/bash

set -e

read -p "Enter the command: " command

case $command in 
    (commit)
        read -p "Enter the commit message : " comment
        read -p "Enter the branch you're in : " branch

        {
            git add .
            git commit -m "$comment"
            git push -u origin "$branch"

            cowsay -f dragon "Changes have been successfully committed and pushed."
        } ||
        {
            cowsay -f dragon "An error occurred during the git operations."
        }
        ;;
    (rebase)
        read -p "Enter the source branch : " sourceBranch
        read -p "Enter the target branch : " targetBranch
        {
            git fetch origin
            git switch "$targetBranch"
            git pull
            git rebase origin/"$sourceBranch"
            git push -f origin "$targetBranch"

            cowsay -f dragon "Rebase operation completed successfully."
        } ||
        {
            cowsay -f dragon "An error occurred during the rebase operation."
        }
        ;;
    (update)
    {
        ./update-project.sh

        cowsay -f dragon "Project has been successfully updated."
    } ||
    {
        cowsay -f dragon "An error occurred during the project update."
    }
esac
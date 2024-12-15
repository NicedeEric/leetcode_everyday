## Generate a new pair of ssh key
ssh-keygen -t ed25519 -C "your_email@example.com"

## Press enter for this prompt
> Enter file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]

## Add SSH key to ssh-agent
Get-Service -Name ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent

## Add SSH key to agent
ssh-add c:/Users/YOU/.ssh/id_ed25519

## Copy the key content
cat ~/.ssh/id_ed25519.pub | clip

## Paste to github in settings/SSH and GPG keys


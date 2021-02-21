# Github
Configurate credentials for clone a private proyect from github


## Create Key
´´´bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
´´´
View SSH-Agent status
´´´bash
ssh-agent
´´´

Launch SSH-Agent in background
´´´bash
eval `ssh-agent -s`
´´´´

Adding a new key file
´´´bash
ssh-keygen -p -f ~/.ssh/id_ed25519
´´´

Forget a key after a seconds.
´´´bash
ssh-add -t <seconds>
´´´´


## Command Usefulls

View ssh keys in server 
´´´bash
cd ~/.ssh
´´´

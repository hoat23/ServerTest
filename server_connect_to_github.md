# Github
Configurate credentials for clone a private proyect from github


## Create Key
creating a private an public key
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
move the key to ```~/.ssh ``` directory
```bash
mv [file-name-rsa] ~/.ssh
mv [file-name-rsa.pub] ~/.ssh
```

add the key to ssh-agent
```bash
ssh-add ~/.ssh/[file-name-rsa]
ssh-keygen -p -f ~/.ssh/[file-name-rsa]
```

## SSH-Agent
View SSH-Agent status
```bash
ssh-agent
```

Launch SSH-Agent in background
```bash
eval `ssh-agent -s`
```

Forget a key after a seconds.
```bash
ssh-add -t <seconds>
```


## Command Usefulls

View ssh keys in server 
```bash
cd ~/.ssh
```

Install 'clip' package to copy information to clipboard
```bash
# copy
sudo apt-get install xclip

# copy to clipboard
xclip -o | xclip -sel clip

# paste
xclip -o -sel clip > file.txt
```




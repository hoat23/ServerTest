# Servidores para multiples pruebas
## Instalar ngrok
mkdir /usr/share/ngrok
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
mv ngrok-stable-linux-amd64.zip /usr/share/ngrok
unzip /usr/share/ngrok/ngrok-stable-linux-amd64.zip

## Ver si se instalo correctamente
./usr/share/ngrok/ngrok -h

## Validar token
./usr/share/ngrok/ngrok autotoken <TOKEN>

## Lanzar ngrok in background
./usr/share/ngrok/ngrok http <PORT>


## Obtener la dirección
curl http://localhost:4040/api/tunnels | json_reformat

## FIN

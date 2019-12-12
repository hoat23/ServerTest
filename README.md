# Servidores para multiples pruebas

https://realpython.com/python-sockets/

## Obtener información del sistema operativo
```
hostnamectl
```
si no funciona probar con 
```
uname -a
```
## Comandos de redes utiles
Ver estado actual de los socket
```
netstat -an
```
```
tcpdump --list-interfaces 
tcpdump -i eth0 -u port 9001
tcpdump -u port 9001
```

```
lsof -i -n
```

## Configurar reloj usando ntpdate
Editar el crontab para q fuerce el actualizado del reloj.
nano /etc/crontab
`*/1 * * * *  root ntpdate pool.ntp.org`

## Servidores disponibles
### Envio de Logs remotos via sockets 
En desarrollo

## Instalar ngrok
```
mkdir /usr/share/ngrok
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
mv ngrok-stable-linux-amd64.zip /usr/share/ngrok
unzip /usr/share/ngrok/ngrok-stable-linux-amd64.zip
```
### Ver si se instalo correctamente
`./usr/share/ngrok/ngrok -h`

### Validar token
`./usr/share/ngrok/ngrok autotoken <TOKEN>`

### Lanzar ngrok in background
`./usr/share/ngrok/ngrok http <PORT>`

### Obtener la dirección ngrok
`curl http://localhost:4040/api/tunnels | json_reformat`

### Otros
Matar procesos por nombre.

`pkill -f "multiprocess_monitor_firewall_ssh.py"`

### Configurar hora en un servidor
```
timedatectl status
timedatectl list-timezones
timedatectl set-timezone 'America/Lima'
```
- Configurar servidor ntp
`yum install ntp`

-Agregar ntp al arranque del sistema

`chkconfig ntp on`

-Iniciar servicio ntp 
```
systemctl ntpd start 
systemctl ntpd status
```

- Filtrar file logs usando grep
 ```
 <log> | grep -v 'input.snmp'
```

## Windows Server  - PowerShell
### Changing Execution Policy
```
Set-ExecutionPolicy Unrestricted
Get-ExecutionPolicy -List
```

## Monitoring snmp of device
### Instaling package to send request snmp in CentOS
```
yum install net-snmp-*
```

### Commands 
```
# Pretty visualization of json
head -1 data.json | jq
```

## Generate SSL certifies using OpenSSL

Link with documentation: 
- https://riptutorial.com/es/openssl/topic/2695/empezando-con-openssl
- https://www.linux-party.com/57-seguridad/9667-generar-fichero-csr-en-linux.html
- https://www.howtoforge.com/tutorial/how-to-install-openssl-from-source-on-linux/

##### Install OpenSSL in Centos
```
yum install openssl openssl-devel 
```
##### Install OpenSSL in Centos

```
apt-get install openssl 
```

Validate version of openssl
```
$ openssl --version
```

### Generete certifies by mcaffe - tcp

https://kc.mcafee.com/corporate/index?page=content&id=KB87927&snspd-1116&locale=es_ES&viewlocale=es_ES

```
openssl req -newkey rsa:2048 -nodes -keyout /etc/owner_certifies/syslogselfsigned.key -x509 -days 365 -out /etc/owner_certifies/syslogselfsigned.crt -config /etc/pki/tls/openssl.cnf
```


### Updating certifies using curl 

Link: https://developers.facebook.com/docs/whatsapp/guides/https

```
curl -X POST \
  https://your-webapp-hostname:your-webapp-port/v1/certificates/external \
  -H 'Authorization: Bearer your-auth-token' \
  -H 'Content-Type: text/plain' \
  --data-binary @your-path-to-certificate.pem 
```
For combine certifies use this command:
```
cat cert1.pem cert2.pem > bundle.pem
```
Uploading ...
```
curl -X POST \
  https://your-webapp-hostname:your-webapp-port/v1/certificates/webhooks/ca \
  -H 'Authorization: Bearer your-auth-token' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: text/plain' \
  --data-binary @your-path-to-certificate.pem \
  -k
```

### Plugins VSCode


#### Encryptor 

@author: Rush Frisby 
@version: 2237
@algorithm: AES 256.

Commands added:

encryptfile - encrypts the entire text in the current document

encryptstr - encrypts only the text that is selected in the current document

decryptfile - decrypts the entire text in the current document

decryptstr - decrypts only the text that is selected in the current document

```
- indent-rainbow
- show-offset
- Docker
```

## CMD in Windows

Show user SID

```
> whoami /user
```

```
> netstat -ano
```

## FIN

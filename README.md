# Servidores para multiples pruebas

https://realpython.com/python-sockets/

## Obtener información del sistema operativo
```
hostnamectl
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


## FIN

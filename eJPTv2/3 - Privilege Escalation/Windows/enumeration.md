# Windows Local Enumeration

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

## Enumerate Users And Groups

```bash
meterpreter > getuid
Server username: WIN-OMCNBKR66MN\Administrator
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

msf5 exploit(windows/http/rejetto_hfs_exec) > use post/windows/gather/enum_logged_on_users

msf5 post(windows/gather/enum_logged_on_users) > options

Module options (post/windows/gather/enum_logged_on_users):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CURRENT  true             yes       Enumerate currently logged on users
   RECENT   true             yes       Enumerate Recently logged on users
   SESSION                   yes       The session to run this module on.

msf5 post(windows/gather/enum_logged_on_users) > set SESSION 1
SESSION => 1
msf5 post(windows/gather/enum_logged_on_users) > run

[*] Running against session 1

Current Logged Users
====================

 SID                                            User
 ---                                            ----
 S-1-5-21-2563855374-3215282501-1490390052-500  WIN-OMCNBKR66MN\Administrator


[+] Results saved in: /root/.msf4/loot/20240402173830_default_10.4.21.46_host.users.activ_108954.txt

Recently Logged Users
=====================

 SID                                            Profile Path
 ---                                            ------------
 S-1-5-18                                       %systemroot%\system32\config\systemprofile
 S-1-5-19                                       C:\Windows\ServiceProfiles\LocalService
 S-1-5-20                                       C:\Windows\ServiceProfiles\NetworkService
 S-1-5-21-2563855374-3215282501-1490390052-500  C:\Users\Administrator


[*] Post module execution completed
```

```bash
C:\hfs>query user
query user
 USERNAME              SESSIONNAME        ID  STATE   IDLE TIME  LOGON TIME
>administrator         console             1  Active      none   4/2/2024 12:04 PM

C:\Windows\system32>net user
net user

User accounts for \\VICTIM

-------------------------------------------------------------------------------
admin                    Administrator            Guest
The command completed successfully.

C:\hfs>net user administrator
net user administrator
User name                    Administrator
Full Name
Comment                      Built-in account for administering the computer/domain
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            9/10/2020 9:10:03 AM
Password expires             Never
Password changeable          9/10/2020 9:10:03 AM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   4/2/2024 12:04:52 PM

Logon hours allowed          All

Local Group Memberships      *Administrators
Global Group memberships     *None
The command completed successfully.


c:\>net user guest
net user guest
User name                    Guest
Full Name                    
Comment                      Built-in account for guest access to the computer/domain
User's comment               
Country/region code          000 (System Default)
Account active               No
Account expires              Never

Password last set            4/2/2024 12:13:34 PM
Password expires             Never
Password changeable          4/2/2024 12:13:34 PM
Password required            No
User may change password     No

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   Never

Logon hours allowed          All

Local Group Memberships      *Guests               
Global Group memberships     *None                 
The command completed successfully.

c:\>net localgroup
net localgroup

Aliases for \\WIN-OMCNBKR66MN

-------------------------------------------------------------------------------
*Access Control Assistance Operators
*Administrators
*Backup Operators
*Certificate Service DCOM Access
*Cryptographic Operators
*Distributed COM Users
*Event Log Readers
*Guests
*Hyper-V Administrators
*IIS_IUSRS
*Network Configuration Operators
*Performance Log Users
*Performance Monitor Users
*Power Users
*Print Operators
*RDS Endpoint Servers
*RDS Management Servers
*RDS Remote Access Servers
*Remote Desktop Users
*Remote Management Users
*Replicator
*Users
*WinRMRemoteWMIUsers__
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


C:\hfs>whoami
whoami
win-omcnbkr66mn\administrator

C:\hfs>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                  Description                               State
=============================== ========================================= =======
SeIncreaseQuotaPrivilege        Adjust memory quotas for a process        Enabled
SeSecurityPrivilege             Manage auditing and security log          Enabled
SeTakeOwnershipPrivilege        Take ownership of files or other objects  Enabled
SeLoadDriverPrivilege           Load and unload device drivers            Enabled
SeSystemProfilePrivilege        Profile system performance                Enabled
SeSystemtimePrivilege           Change the system time                    Enabled
SeProfileSingleProcessPrivilege Profile single process                    Enabled
SeIncreaseBasePriorityPrivilege Increase scheduling priority              Enabled
SeCreatePagefilePrivilege       Create a pagefile                         Enabled
SeBackupPrivilege               Back up files and directories             Enabled
SeRestorePrivilege              Restore files and directories             Enabled
SeShutdownPrivilege             Shut down the system                      Enabled
SeDebugPrivilege                Debug programs                            Enabled
SeSystemEnvironmentPrivilege    Modify firmware environment values        Enabled
SeChangeNotifyPrivilege         Bypass traverse checking                  Enabled
SeRemoteShutdownPrivilege       Force shutdown from a remote system       Enabled
SeUndockPrivilege               Remove computer from docking station      Enabled
SeManageVolumePrivilege         Perform volume maintenance tasks          Enabled
SeImpersonatePrivilege          Impersonate a client after authentication Enabled
SeCreateGlobalPrivilege         Create global objects                     Enabled
SeIncreaseWorkingSetPrivilege   Increase a process working set            Enabled
SeTimeZonePrivilege             Change the time zone                      Enabled
SeCreateSymbolicLinkPrivilege   Create symbolic links                     Enabled
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

## Enumerating Network Information

```bash
C:\hfs>ipconfig
ipconfig

Windows IP Configuration


Ethernet adapter Ethernet 3:

   Connection-specific DNS Suffix  . : ec2.internal
   Link-local IPv6 Address . . . . . : fe80::e4bc:fd09:7dc1:377e%22
   IPv4 Address. . . . . . . . . . . : 10.4.27.84
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . : 10.4.16.1

Tunnel adapter isatap.ec2.internal:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : ec2.internal

C:\hfs>ipconfig /all
ipconfig /all

Windows IP Configuration

   Host Name . . . . . . . . . . . . : WIN-OMCNBKR66MN
   Primary Dns Suffix  . . . . . . . : 
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : ap-southeast-1.ec2-utilities.amazonaws.com
                                       us-east-1.ec2-utilities.amazonaws.com
                                       ap-southeast-1.compute.internal
                                       ec2.internal

Ethernet adapter Ethernet 3:

   Connection-specific DNS Suffix  . : ec2.internal
   Description . . . . . . . . . . . : Amazon Elastic Network Adapter
   Physical Address. . . . . . . . . : 0E-BA-57-3D-E6-19
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::e4bc:fd09:7dc1:377e%22(Preferred) 
   IPv4 Address. . . . . . . . . . . : 10.4.27.84(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Lease Obtained. . . . . . . . . . : Wednesday, April 3, 2024 9:49:30 AM
   Lease Expires . . . . . . . . . . : Wednesday, April 3, 2024 10:49:29 AM
   Default Gateway . . . . . . . . . : 10.4.16.1
   DHCP Server . . . . . . . . . . . : 10.4.16.1
   DHCPv6 IAID . . . . . . . . . . . : 370063959
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-26-EB-A5-6A-06-4E-FA-4C-65-EA
   DNS Servers . . . . . . . . . . . : 10.4.0.2
   NetBIOS over Tcpip. . . . . . . . : Enabled

Tunnel adapter isatap.ec2.internal:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : ec2.internal
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter #2
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

C:\hfs>route print
route print
===========================================================================
Interface List
 22...0e ba 57 3d e6 19 ......Amazon Elastic Network Adapter
  1...........................Software Loopback Interface 1
 15...00 00 00 00 00 00 00 e0 Microsoft ISATAP Adapter #2
===========================================================================

IPv4 Route Table
===========================================================================
Active Routes:
Network Destination        Netmask          Gateway       Interface  Metric
          0.0.0.0          0.0.0.0        10.4.16.1       10.4.27.84      5
        10.4.16.0    255.255.240.0         On-link        10.4.27.84    261
       10.4.27.84  255.255.255.255         On-link        10.4.27.84    261
      10.4.31.255  255.255.255.255         On-link        10.4.27.84    261
        127.0.0.0        255.0.0.0         On-link         127.0.0.1    306
        127.0.0.1  255.255.255.255         On-link         127.0.0.1    306
  127.255.255.255  255.255.255.255         On-link         127.0.0.1    306
  169.254.169.123  255.255.255.255        10.4.16.1       10.4.27.84      5
  169.254.169.249  255.255.255.255        10.4.16.1       10.4.27.84      5
  169.254.169.250  255.255.255.255        10.4.16.1       10.4.27.84      5
  169.254.169.251  255.255.255.255        10.4.16.1       10.4.27.84      5
  169.254.169.253  255.255.255.255        10.4.16.1       10.4.27.84      5
  169.254.169.254  255.255.255.255        10.4.16.1       10.4.27.84      5
        224.0.0.0        240.0.0.0         On-link         127.0.0.1    306
        224.0.0.0        240.0.0.0         On-link        10.4.27.84    261
  255.255.255.255  255.255.255.255         On-link         127.0.0.1    306
  255.255.255.255  255.255.255.255         On-link        10.4.27.84    261
===========================================================================
Persistent Routes:
  None

IPv6 Route Table
===========================================================================
Active Routes:
 If Metric Network Destination      Gateway
  1    306 ::1/128                  On-link
 22    261 fe80::/64                On-link
 22    261 fe80::e4bc:fd09:7dc1:377e/128
                                    On-link
  1    306 ff00::/8                 On-link
 22    261 ff00::/8                 On-link
===========================================================================
Persistent Routes:
  None


C:\hfs>arp -a
arp -a

Interface: 10.4.27.84 --- 0x16
  Internet Address      Physical Address      Type
  10.4.16.1             0e-ef-4e-ab-e7-33     dynamic   
  10.4.22.37            0e-cd-35-10-3e-ff     dynamic   
  10.4.26.187           0e-e7-07-83-7b-35     dynamic   
  10.4.29.144           0e-36-89-16-fa-f9     dynamic   
  10.4.31.255           ff-ff-ff-ff-ff-ff     static    
  224.0.0.22            01-00-5e-00-00-16     static    
  224.0.0.252           01-00-5e-00-00-fc     static    
  255.255.255.255       ff-ff-ff-ff-ff-ff     static    

C:\hfs>netstat -ano
netstat -ano

Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING       2768
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       608
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING       1824
  TCP    0.0.0.0:5985           0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:47001          0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:49152          0.0.0.0:0              LISTENING       400
  TCP    0.0.0.0:49153          0.0.0.0:0              LISTENING       692
  TCP    0.0.0.0:49154          0.0.0.0:0              LISTENING       740
  TCP    0.0.0.0:49155          0.0.0.0:0              LISTENING       340
  TCP    0.0.0.0:49166          0.0.0.0:0              LISTENING       496
  TCP    0.0.0.0:49180          0.0.0.0:0              LISTENING       488
  TCP    10.4.27.84:139         0.0.0.0:0              LISTENING       4
  TCP    10.4.27.84:49217       10.4.29.144:443        ESTABLISHED     396
  TCP    10.4.27.84:49254       10.10.22.2:4444        ESTABLISHED     2920
  TCP    10.4.27.84:49327       169.254.169.254:80     TIME_WAIT       0
  TCP    10.4.27.84:49347       10.4.22.37:443         ESTABLISHED     396
  TCP    127.0.0.1:80           127.0.0.1:49348        ESTABLISHED     2768
  TCP    127.0.0.1:80           127.0.0.1:49349        ESTABLISHED     2768
  TCP    127.0.0.1:80           127.0.0.1:49350        ESTABLISHED     2768
  TCP    127.0.0.1:49348        127.0.0.1:80           ESTABLISHED     2656
  TCP    127.0.0.1:49349        127.0.0.1:80           ESTABLISHED     2656
  TCP    127.0.0.1:49350        127.0.0.1:80           ESTABLISHED     2656
  TCP    [::]:135               [::]:0                 LISTENING       608
  TCP    [::]:445               [::]:0                 LISTENING       4
  TCP    [::]:3389              [::]:0                 LISTENING       1824
  TCP    [::]:5985              [::]:0                 LISTENING       4
  TCP    [::]:47001             [::]:0                 LISTENING       4
  TCP    [::]:49152             [::]:0                 LISTENING       400
  TCP    [::]:49153             [::]:0                 LISTENING       692
  TCP    [::]:49154             [::]:0                 LISTENING       740
  TCP    [::]:49155             [::]:0                 LISTENING       340
  TCP    [::]:49166             [::]:0                 LISTENING       496
  TCP    [::]:49180             [::]:0                 LISTENING       488
  UDP    0.0.0.0:500            *:*                                    740
  UDP    0.0.0.0:3389           *:*                                    1824
  UDP    0.0.0.0:4500           *:*                                    740
  UDP    0.0.0.0:5355           *:*                                    860
  UDP    10.4.27.84:137         *:*                                    4
  UDP    10.4.27.84:138         *:*                                    4
  UDP    [::]:500               *:*                                    740
  UDP    [::]:3389              *:*                                    1824
  UDP    [::]:4500              *:*                                    740
  UDP    [::]:5355              *:*                                    860


C:\hfs>netsh advfirewall
netsh advfirewall

The following commands are available:

Commands in this context:
?              - Displays a list of commands.
consec         - Changes to the `netsh advfirewall consec' context.
dump           - Displays a configuration script.
export         - Exports the current policy to a file.
firewall       - Changes to the `netsh advfirewall firewall' context.
help           - Displays a list of commands.
import         - Imports a policy file into the current policy store.
mainmode       - Changes to the `netsh advfirewall mainmode' context.
monitor        - Changes to the `netsh advfirewall monitor' context.
reset          - Resets the policy to the default out-of-box policy.
set            - Sets the per-profile or global settings.
show           - Displays profile or global properties.

The following sub-contexts are available:
 consec firewall mainmode monitor

To view help for a command, type the command, followed by a space, and then
 type ?.



C:\hfs>netsh advfirewall show allprofiles
netsh advfirewall show allprofiles

An error occurred while attempting to contact the  Windows Firewall service. Make sure that the service is running and try your request again.
```

## Enumerating Processes & Services

```bash
meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                           Path
 ---   ----  ----                  ----  -------  ----                           ----
 0     0     [System Process]                                                    
 4     0     System                x64   0                                       
 240   4     smss.exe              x64   0                                       
 292   492   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM            C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe
 324   492   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM            C:\Windows\System32\spoolsv.exe
 332   324   csrss.exe             x64   0                                       
 396   324   wininit.exe           x64   0        NT AUTHORITY\SYSTEM            C:\Windows\System32\wininit.exe
 404   388   csrss.exe             x64   1                                       
 432   388   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM            C:\Windows\System32\winlogon.exe
 492   396   services.exe          x64   0                                       
 500   396   lsass.exe             x64   0        NT AUTHORITY\SYSTEM            C:\Windows\System32\lsass.exe
 548   492   svchost.exe           x64   0        NT AUTHORITY\SYSTEM            C:\Windows\System32\svchost.exe
 564   492   svchost.exe           x64   0        NT AUTHORITY\SYSTEM            C:\Windows\System32\svchost.exe
 604   492   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE   C:\Windows\System32\svchost.exe
 680   432   dwm.exe               x64   1        Window Manager\DWM-1           C:\Windows\System32\dwm.exe
 688   492   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE     C:\Windows\System32\svchost.exe
 720   492   svchost.exe           x64   0        NT AUTHORITY\SYSTEM            C:\Windows\System32\svchost.exe
 736   492   svchost.exe           x64   0        NT AUTHORITY\SYSTEM            C:\Windows\System32\svchost.exe
 760   492   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE     C:\Windows\System32\svchost.exe
 876   492   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE   C:\Windows\System32\svchost.exe
 1020  492   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE     C:\Windows\System32\svchost.exe
 1028  492   svchost.exe           x64   0        NT AUTHORITY\SYSTEM            C:\Windows\System32\svchost.exe
 1100  492   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM            C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe
 1420  564   WmiPrvSE.exe          x64   0        NT AUTHORITY\NETWORK SERVICE   C:\Windows\System32\wbem\WmiPrvSE.exe
 1560  720   taskhost.exe          x64   0        NT AUTHORITY\SYSTEM            C:\Windows\System32\taskhost.exe
 1824  492   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE   C:\Windows\System32\svchost.exe
 1852  3020  hfs.exe               x86   1        WIN-OMCNBKR66MN\Administrator  C:\hfs\hfs.exe
 1916  492   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE   C:\Windows\System32\svchost.exe
 1936  2816  yMBUAxVcAzDG.exe      x86   1        WIN-OMCNBKR66MN\Administrator  C:\Users\ADMINI~1\AppData\Local\Temp\1\rad4F345.tmp\yMBUAxVcAzDG.exe
 1940  720   taskhostex.exe        x64   0        NT AUTHORITY\SYSTEM            C:\Windows\System32\taskhostex.exe
 1952  564   TiWorker.exe          x64   0        NT AUTHORITY\SYSTEM            C:\Windows\WinSxS\amd64_microsoft-windows-servicingstack_31bf3856ad364e35_6.3.9600.19750_none_fa39f32f9b2d0928\TiWorker.exe
 2096  1936  cmd.exe               x86   1        WIN-OMCNBKR66MN\Administrator  C:\Windows\SysWOW64\cmd.exe
 2224  720   taskhostex.exe        x64   1        WIN-OMCNBKR66MN\Administrator  C:\Windows\System32\taskhostex.exe
 2324  2260  explorer.exe          x64   1        WIN-OMCNBKR66MN\Administrator  C:\Windows\explorer.exe
 2336  492   msdtc.exe             x64   0        NT AUTHORITY\NETWORK SERVICE   C:\Windows\System32\msdtc.exe
 2768  492   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM            C:\Windows\servicing\TrustedInstaller.exe
 2816  1852  wscript.exe           x86   1        WIN-OMCNBKR66MN\Administrator  C:\Windows\SysWOW64\wscript.exe
 3008  2096  conhost.exe           x64   1        WIN-OMCNBKR66MN\Administrator  C:\Windows\System32\conhost.exe
 3020  2324  powershell.exe        x86   1        WIN-OMCNBKR66MN\Administrator  C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
 3028  3020  conhost.exe           x64   1        WIN-OMCNBKR66MN\Administrator  C:\Windows\System32\conhost.exe


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

meterpreter > pgrep explorer
2324

meterpreter > migrate 2324
[*] Migrating from 2544 to 2324...
[*] Migration completed successfully.

meterpreter > getuid 
Server username: WIN-OMCNBKR66MN\Administrator

meterpreter > sysinfo 
Computer        : WIN-OMCNBKR66MN
OS              : Windows 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x64/windows
```

List Started services
```bash
C:\Windows\system32>net start
net start
These Windows services are started:

   Amazon SSM Agent
   Application Experience
   Background Tasks Infrastructure Service
   Base Filtering Engine
   Certificate Propagation
   CNG Key Isolation
   COM+ Event System
   Cryptographic Services
   DCOM Server Process Launcher
   Device Install Service
   Device Setup Manager
   DHCP Client
   Diagnostic Policy Service
   Diagnostics Tracking Service
   Distributed Link Tracking Client
   Distributed Transaction Coordinator
   DNS Client
   Ec2Config
   Group Policy Client
   IKE and AuthIP IPsec Keying Modules
   IP Helper
   IPsec Policy Agent
   Local Session Manager
   Network List Service
   Network Location Awareness
   Network Store Interface Service
   Plug and Play
   Power
   Print Spooler
   Remote Desktop Configuration
   Remote Desktop Services
   Remote Desktop Services UserMode Port Redirector
   Remote Procedure Call (RPC)
   RPC Endpoint Mapper
   Security Accounts Manager
   Server
   Shell Hardware Detection
   System Event Notification Service
   System Events Broker
   Task Scheduler
   TCP/IP NetBIOS Helper
   Themes
   User Access Logging Service
   User Profile Service
   Windows Connection Manager
   Windows Event Log
   Windows Font Cache Service
   Windows Management Instrumentation
   Windows Modules Installer
   Windows Remote Management (WS-Management)
   Windows Time
   WinHTTP Web Proxy Auto-Discovery Service
   Workstation

The command completed successfully.

# All services
C:\Windows\system32>wmic service list brief
wmic service list brief
ExitCode  Name                      ProcessId  StartMode  State    Status  
0         AeLookupSvc               720        Manual     Running  OK      
1077      ALG                       0          Manual     Stopped  OK      
0         AmazonSSMAgent            292        Auto       Running  OK      
1077      AppIDSvc                  0          Manual     Stopped  OK      
1077      Appinfo                   0          Manual     Stopped  OK      
1077      AppMgmt                   0          Manual     Stopped  OK      
1077      AppReadiness              0          Manual     Stopped  OK      
1077      AppXSvc                   0          Manual     Stopped  OK      
1077      AudioEndpointBuilder      0          Manual     Stopped  OK      
1077      Audiosrv                  0          Manual     Stopped  OK      
0         AWSLiteAgent              0          Auto       Stopped  OK      
0         BFE                       1020       Auto       Running  OK      
1077      BITS                      0          Manual     Stopped  OK      
0         BrokerInfrastructure      564        Auto       Running  OK      
1077      Browser                   0          Disabled   Stopped  OK      
0         CertPropSvc               720        Manual     Running  OK      
1077      cfn-hup                   0          Manual     Stopped  OK      
1077      COMSysApp                 0          Manual     Stopped  OK      
0         CryptSvc                  876        Auto       Running  OK      
0         DcomLaunch                564        Auto       Running  OK      
0         defragsvc                 0          Manual     Stopped  OK      
1077      DeviceAssociationService  0          Manual     Stopped  OK      
0         DeviceInstall             564        Manual     Running  OK      
0         Dhcp                      688        Auto       Running  OK      
0         DiagTrack                 736        Auto       Running  OK      
0         Dnscache                  876        Auto       Running  OK      
1077      dot3svc                   0          Manual     Stopped  OK      
0         DPS                       1020       Auto       Running  OK      
0         DsmSvc                    720        Manual     Running  OK      
1077      Eaphost                   0          Manual     Stopped  OK      
0         Ec2Config                 1100       Auto       Running  OK      
1077      EFS                       0          Manual     Stopped  OK      
0         EventLog                  688        Auto       Running  OK      
0         EventSystem               760        Auto       Running  OK      
1077      fdPHost                   0          Manual     Stopped  OK      
1077      FDResPub                  0          Manual     Stopped  OK      
0         FontCache                 760        Auto       Running  OK      
0         gpsvc                     720        Auto       Running  OK      
1077      hidserv                   0          Manual     Stopped  OK      
1077      hkmsvc                    0          Manual     Stopped  OK      
1077      IEEtwCollectorService     0          Manual     Stopped  OK      
0         IKEEXT                    720        Auto       Running  OK      
0         iphlpsvc                  720        Auto       Running  OK      
0         KeyIso                    500        Manual     Running  OK      
1077      KPSSVC                    0          Manual     Stopped  OK      
1077      KtmRm                     0          Manual     Stopped  OK      
0         LanmanServer              720        Auto       Running  OK      
0         LanmanWorkstation         876        Auto       Running  OK      
1077      lltdsvc                   0          Manual     Stopped  OK      
0         lmhosts                   688        Auto       Running  OK      
0         LSM                       564        Auto       Running  OK      
1077      MMCSS                     0          Manual     Stopped  OK      
1077      MozillaMaintenance        0          Manual     Stopped  OK      
1077      MpsSvc                    0          Disabled   Stopped  OK      
0         MSDTC                     2336       Auto       Running  OK      
1077      MSiSCSI                   0          Manual     Stopped  OK      
1077      msiserver                 0          Manual     Stopped  OK      
1077      napagent                  0          Manual     Stopped  OK      
1077      NcaSvc                    0          Manual     Stopped  OK      
1077      Netlogon                  0          Manual     Stopped  OK      
1077      Netman                    0          Manual     Stopped  OK      
0         netprofm                  760        Manual     Running  OK      
1077      NetTcpPortSharing         0          Disabled   Stopped  OK      
0         NlaSvc                    876        Auto       Running  OK      
0         nsi                       760        Auto       Running  OK      
1077      PerfHost                  0          Manual     Stopped  OK      
1077      pla                       0          Manual     Stopped  OK      
0         PlugPlay                  564        Manual     Running  OK      
0         PolicyAgent               1916       Manual     Running  OK      
0         Power                     564        Auto       Running  OK      
1077      PrintNotify               0          Manual     Stopped  OK      
0         ProfSvc                   720        Auto       Running  OK      
1077      RasAuto                   0          Manual     Stopped  OK      
1077      RasMan                    0          Manual     Stopped  OK      
1077      RemoteAccess              0          Disabled   Stopped  OK      
...

C:\Windows\system32>tasklist /SVC
tasklist /SVC

Image Name                     PID Services                                    
========================= ======== ============================================
System Idle Process              0 N/A                                         
System                           4 N/A                                         
smss.exe                       240 N/A                                         
csrss.exe                      332 N/A                                         
wininit.exe                    396 N/A                                         
csrss.exe                      404 N/A                                         
winlogon.exe                   432 N/A                                         
services.exe                   492 N/A                                         
lsass.exe                      500 KeyIso, SamSs                               
svchost.exe                    564 BrokerInfrastructure, DcomLaunch,           
                                   DeviceInstall, LSM, PlugPlay, Power,        
                                   SystemEventsBroker                          
svchost.exe                    604 RpcEptMapper, RpcSs                         
dwm.exe                        680 N/A                                         
svchost.exe                    688 Dhcp, EventLog, lmhosts, Wcmsvc             
svchost.exe                    720 AeLookupSvc, CertPropSvc, DsmSvc, gpsvc,    
                                   IKEEXT, iphlpsvc, LanmanServer, ProfSvc,    
                                   Schedule, SENS, SessionEnv,                 
                                   ShellHWDetection, Themes, Winmgmt           
svchost.exe                    760 EventSystem, FontCache, netprofm, nsi,      
                                   W32Time, WinHttpAutoProxySvc                
svchost.exe                    876 CryptSvc, Dnscache, LanmanWorkstation,      
                                   NlaSvc, WinRM                               
svchost.exe                   1020 BFE, DPS                                    
spoolsv.exe                    324 Spooler                                     
amazon-ssm-agent.exe           292 AmazonSSMAgent                              
svchost.exe                    736 DiagTrack                                   
svchost.exe                   1028 TrkWks, UALSVC, UmRdpService                
Ec2Config.exe                 1100 Ec2Config                                   
WmiPrvSE.exe                  1420 N/A                                         
svchost.exe                   1824 TermService                                 
svchost.exe                   1916 PolicyAgent                                 
taskhostex.exe                2224 N/A                                         
explorer.exe                  2324 N/A                                         
powershell.exe                3020 N/A                                         
conhost.exe                   3028 N/A                                         
hfs.exe                       1852 N/A                                         
cmd.exe                       2096 N/A                                         
conhost.exe                   3008 N/A                                         
msdtc.exe                     2336 MSDTC                                       
TrustedInstaller.exe          2768 TrustedInstaller                            
TiWorker.exe                  1952 N/A                                         
cmd.exe                       1836 N/A                                         
conhost.exe                   1832 N/A                                         
cmd.exe                       2156 N/A                                         
conhost.exe                   2372 N/A                                         
cmd.exe                       2760 N/A                                         
conhost.exe                    548 N/A                                         
cmd.exe                       1592 N/A                                         
conhost.exe                    464 N/A                                         
WmiPrvSE.exe                   960 N/A                                         
tasklist.exe                  2560 N/A                                         


C:\Windows\system32>schtasks /query /fo LIST
schtasks /query /fo LIST

Folder: \
HostName:      WIN-OMCNBKR66MN
TaskName:      \Ec2ConfigMonitorTask
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Ec2ConfigMonitorTask
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Optimize Start Menu Cache Files-S-1-5-21-2563855374-3215282501-1490390052-500
Next Run Time: N/A
Status:        Disabled
Logon Mode:    Interactive only

Folder: \Microsoft
INFO: There are no scheduled tasks presently available at your access level.

Folder: \Microsoft\Windows
INFO: There are no scheduled tasks presently available at your access level.

Folder: \Microsoft\Windows\.NET Framework
HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 64 Critical
Next Run Time: N/A
Status:        Disabled
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\.NET Framework\.NET Framework NGEN v4.0.30319 Critical
Next Run Time: N/A
Status:        Disabled
Logon Mode:    Interactive/Background

Folder: \Microsoft\Windows\Active Directory Rights Management Services Client
HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\Active Directory Rights Management Services Client\AD RMS Rights Policy Template Management (Automated)
Next Run Time: N/A
Status:        Disabled
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\Active Directory Rights Management Services Client\AD RMS Rights Policy Template Management (Automated)
Next Run Time: N/A
Status:        Disabled
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\Active Directory Rights Management Services Client\AD RMS Rights Policy Template Management (Manual)
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

Folder: \Microsoft\Windows\AppID
HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\AppID\PolicyConverter
Next Run Time: N/A
Status:        Disabled
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\AppID\SmartScreenSpecific
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\AppID\VerifiedPublisherCertStoreCheck
Next Run Time: N/A
Status:        Disabled
Logon Mode:    Interactive/Background

Folder: \Microsoft\Windows\Application Experience
HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\Application Experience\AitAgent
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser
Next Run Time: 4/4/2024 1:00:31 AM
Status:        Ready
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\Application Experience\ProgramDataUpdater
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

Folder: \Microsoft\Windows\ApplicationData
HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\ApplicationData\CleanupTemporaryState
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

Folder: \Microsoft\Windows\AppxDeploymentClient
HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\AppxDeploymentClient\Pre-staged app cleanup
Next Run Time: N/A
Status:        Disabled
Logon Mode:    Interactive/Background

Folder: \Microsoft\Windows\Autochk
HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\Autochk\Proxy
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

Folder: \Microsoft\Windows\CertificateServicesClient
HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\CertificateServicesClient\SystemTask
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\CertificateServicesClient\SystemTask
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\CertificateServicesClient\SystemTask
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

HostName:      WIN-OMCNBKR66MN
TaskName:      \Microsoft\Windows\CertificateServicesClient\UserTask
Next Run Time: N/A
Status:        Ready
Logon Mode:    Interactive/Background

...

C:\Windows\system32>schtasks /query /fo LIST /v

...
HostName:                             WIN-OMCNBKR66MN
TaskName:                             \Microsoft\Windows\Windows Error Reporting\QueueReporting
Next Run Time:                        N/A
Status:                               Ready
Logon Mode:                           Interactive/Background
Last Run Time:                        4/3/2024 10:18:58 AM
Last Result:                          0
Author:                               Microsoft Corporation
Task To Run:                          %windir%\system32\wermgr.exe -queuereporting
Start In:                             N/A
Comment:                              Windows Error Reporting task to process queued reports.
Scheduled Task State:                 Enabled
Idle Time:                            Disabled
Power Management:                     No Start On Batteries
Run As User:                          Users
Delete Task If Not Rescheduled:       Disabled
Stop Task If Runs X Hours and X Mins: 72:00:00
Schedule:                             Scheduling data is not available in this format.
Schedule Type:                        When an event occurs
Start Time:                           N/A
Start Date:                           N/A
End Date:                             N/A
Days:                                 N/A
Months:                               N/A
Repeat: Every:                        N/A
Repeat: Until: Time:                  N/A
Repeat: Until: Duration:              N/A
Repeat: Stop If Still Running:        N/A

Folder: \Microsoft\Windows\Windows Filtering Platform
HostName:                             WIN-OMCNBKR66MN
TaskName:                             \Microsoft\Windows\Windows Filtering Platform\BfeOnServiceStartTypeChange
Next Run Time:                        N/A
Status:                               Ready
Logon Mode:                           Interactive/Background
Last Run Time:                        N/A
Last Result:                          1
Author:                               Microsoft Corporation
Task To Run:                          %windir%\system32\rundll32.exe bfe.dll,BfeOnServiceStartTypeChange
Start In:                             N/A
Comment:                              This task adjusts the start type for firewall-triggered services when the start type of the Base Filtering Engine (BFE) is disabled.
Scheduled Task State:                 Enabled
Idle Time:                            Disabled
Power Management:                     
Run As User:                          SYSTEM
Delete Task If Not Rescheduled:       Disabled
Stop Task If Runs X Hours and X Mins: 72:00:00
Schedule:                             Scheduling data is not available in this format.
Schedule Type:                        When an event occurs
Start Time:                           N/A
Start Date:                           N/A
End Date:                             N/A
Days:                                 N/A
Months:                               N/A
Repeat: Every:                        N/A
Repeat: Until: Time:                  N/A
Repeat: Until: Duration:              N/A
Repeat: Stop If Still Running:        N/A

Folder: \Microsoft\Windows\WindowsColorSystem
HostName:                             WIN-OMCNBKR66MN
TaskName:                             \Microsoft\Windows\WindowsColorSystem\Calibration Loader
Next Run Time:                        N/A
Status:                               Disabled
Logon Mode:                           Interactive/Background
Last Run Time:                        8/22/2013 2:50:26 PM
Last Result:                          0
Author:                               Microsoft Corporation
Task To Run:                          COM handler
Start In:                             N/A
Comment:                              This task applies color calibration settings.
Scheduled Task State:                 Disabled
Idle Time:                            Disabled
Power Management:                     
Run As User:                          Users
Delete Task If Not Rescheduled:       Disabled
Stop Task If Runs X Hours and X Mins: Disabled
Schedule:                             Scheduling data is not available in this format.
Schedule Type:                        At logon time
Start Time:                           N/A
Start Date:                           N/A
End Date:                             N/A
Days:                                 N/A
Months:                               N/A
Repeat: Every:                        N/A
Repeat: Until: Time:                  N/A
Repeat: Until: Duration:              N/A
Repeat: Stop If Still Running:        N/A

HostName:                             WIN-OMCNBKR66MN
TaskName:                             \Microsoft\Windows\WindowsColorSystem\Calibration Loader
Next Run Time:                        N/A
Status:                               Disabled
Logon Mode:                           Interactive/Background
Last Run Time:                        8/22/2013 2:50:26 PM
Last Result:                          0
Author:                               Microsoft Corporation
Task To Run:                          COM handler
Start In:                             N/A
Comment:                              This task applies color calibration settings.
Scheduled Task State:                 Disabled
Idle Time:                            Disabled
Power Management:                     
Run As User:                          Users
Delete Task If Not Rescheduled:       Disabled
Stop Task If Runs X Hours and X Mins: Disabled
Schedule:                             Scheduling data is not available in this format.
Schedule Type:                        When an event occurs
Start Time:                           N/A
Start Date:                           N/A
End Date:                             N/A
Days:                                 N/A
Months:                               N/A
Repeat: Every:                        N/A
Repeat: Until: Time:                  N/A
Repeat: Until: Duration:              N/A
Repeat: Stop If Still Running:        N/A

Folder: \Microsoft\Windows\WindowsUpdate
HostName:                             WIN-OMCNBKR66MN
TaskName:                             \Microsoft\Windows\WindowsUpdate\AUFirmwareInstall
Next Run Time:                        N/A
Status:                               Disabled
Logon Mode:                           Interactive/Background
Last Run Time:                        N/A
Last Result:                          1
Author:                               Microsoft Corporation.
Task To Run:                          COM handler
Start In:                             N/A
Comment:                              This task is used to install firmware updates on the machine.
Scheduled Task State:                 Disabled
Idle Time:                            Disabled
Power Management:                     
Run As User:                          LOCAL SERVICE
Delete Task If Not Rescheduled:       Disabled
Stop Task If Runs X Hours and X Mins: 72:00:00
Schedule:                             Scheduling data is not available in this format.
Schedule Type:                        Undefined
Start Time:                           N/A
Start Date:                           N/A
End Date:                             N/A
Days:                                 N/A
Months:                               N/A
Repeat: Every:                        N/A
Repeat: Until: Time:                  N/A
Repeat: Until: Duration:              N/A
Repeat: Stop If Still Running:        N/A

....
```

## Disk Mounts

```bash
meterpreter > show_mount 

Mounts / Drives
===============

Name  Type   Size (Total)  Size (Free)  Mapped to
----  ----   ------------  -----------  ---------
C:\   fixed  30.00 GiB     16.27 GiB    


Total mounts/drives: 1
```

## Automating Windows Local Enumeration

JAWS - Just Another Windows (Enum) Script
https://github.com/411Hall/JAWS
(haven't been updated in 5 years, use WinPEAS)


## More Enumeration

```bash
msf6 exploit(windows/winrm/winrm_script_exec) > use post/windows/gather/win_privs

msf6 post(windows/gather/win_privs) > set SESSION 1
SESSION => 1

msf6 post(windows/gather/win_privs) > run

Current User
============

 Is Admin  Is System  Is In Local Admin Group  UAC Enabled  Foreground ID  UID
 --------  ---------  -----------------------  -----------  -------------  ---
 True      True       True                     False        1              NT AUTHORITY\SYSTEM

Windows Privileges
==================

 Name
 ----
 SeAssignPrimaryTokenPrivilege
 SeAuditPrivilege
 SeBackupPrivilege
 SeChangeNotifyPrivilege
 SeCreateGlobalPrivilege
 SeCreatePagefilePrivilege
 SeCreatePermanentPrivilege
 SeCreateSymbolicLinkPrivilege
 SeDebugPrivilege
 SeImpersonatePrivilege
 SeIncreaseBasePriorityPrivilege
 SeIncreaseQuotaPrivilege
 SeIncreaseWorkingSetPrivilege
 SeLoadDriverPrivilege
 SeLockMemoryPrivilege
 SeManageVolumePrivilege
 SeProfileSingleProcessPrivilege
 SeRestorePrivilege
 SeSecurityPrivilege
 SeShutdownPrivilege
 SeSystemEnvironmentPrivilege
 SeSystemProfilePrivilege
 SeSystemtimePrivilege
 SeTakeOwnershipPrivilege
 SeTcbPrivilege
 SeTimeZonePrivilege
 SeUndockPrivilege

[*] Post module execution completed

msf6 post(windows/gather/win_privs) > use post/windows/gather/enum_logged_on_users
msf6 post(windows/gather/enum_logged_on_users) > options

Module options (post/windows/gather/enum_logged_on_users):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CURRENT  true             yes       Enumerate currently logged on users
   RECENT   true             yes       Enumerate Recently logged on users
   SESSION  1                yes       The session to run this module on.

msf6 post(windows/gather/enum_logged_on_users) > run

[*] Running against session 1

Current Logged Users
====================

 SID                                            User
 ---                                            ----
 S-1-5-18                                       NT AUTHORITY\SYSTEM
 S-1-5-21-1560653127-1539696675-2954027093-500  SERVER\Administrator


[+] Results saved in: /root/.msf4/loot/20240403170006_default_10.4.18.118_host.users.activ_276370.txt

Recently Logged Users
=====================

 SID                                            Profile Path
 ---                                            ------------
 S-1-5-18                                       %systemroot%\system32\config\systemprofile
 S-1-5-19                                       %systemroot%\ServiceProfiles\LocalService
 S-1-5-20                                       %systemroot%\ServiceProfiles\NetworkService
 S-1-5-21-1560653127-1539696675-2954027093-500  C:\Users\Administrator


[*] Post module execution completed

msf6 post(windows/gather/enum_logged_on_users) > search checkvm

Matching Modules
================

   #  Name                         Disclosure Date  Rank    Check  Description
   -  ----                         ---------------  ----    -----  -----------
   0  post/linux/gather/checkvm                     normal  No     Linux Gather Virtual Environment Detection
   1  post/solaris/gather/checkvm                   normal  No     Solaris Gather Virtual Environment Detection
   2  post/windows/gather/checkvm                   normal  No     Windows Gather Virtual Environment Detection


Interact with a module by name or index. For example info 2, use 2 or use post/windows/gather/checkvm

msf6 post(windows/gather/enum_logged_on_users) > use post/windows/gather/checkvm
msf6 post(windows/gather/checkvm) > options

Module options (post/windows/gather/checkvm):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION  1                yes       The session to run this module on.

msf6 post(windows/gather/checkvm) > run

[*] Checking if SERVER is a Virtual Machine ...
[+] This is a Xen Virtual Machine
[*] Post module execution completed

msf6 post(windows/gather/checkvm) > use post/windows/gather/enum_applications
msf6 post(windows/gather/enum_applications) > run

[*] Enumerating applications installed on SERVER

Installed Applications
======================

 Name                   Version
 ----                   -------
 AWS PV Drivers         8.3.4
 AWS Tools for Windows  3.15.1110
 Amazon SSM Agent       2.3.1319.0
 Amazon SSM Agent       2.3.1319.0
 aws-cfn-bootstrap      1.4.33


[+] Results stored in: /root/.msf4/loot/20240403170143_default_10.4.18.118_host.application_279967.txt
[*] Post module execution completed


msf6 post(windows/gather/enum_applications) > use post/windows/gather/enum_computers
msf6 post(windows/gather/enum_computers) > run

[*] Running module against SERVER
[-] This host is not part of a domain.
[*] Post module execution completed


msf6 post(windows/gather/enum_computers) > use post/windows/gather/enum_patches
msf6 post(windows/gather/enum_patches) > run

[*] Patch list saved to /root/.msf4/loot/20240403170327_default_10.4.18.118_enum_patches_297439.txt
[+] KB4570720 installed on 9/9/2020
[+] KB4470502 installed on 12/12/2018
[+] KB4470788 installed on 12/12/2018
[+] KB4480056 installed on 1/9/2019
[+] KB4493510 installed on 4/21/2019
[+] KB4494174 installed on 3/18/2020
[+] KB4499728 installed on 5/15/2019
[+] KB4504369 installed on 6/12/2019
[+] KB4512577 installed on 9/11/2019
[+] KB4512937 installed on 9/6/2019
[+] KB4521862 installed on 10/9/2019
[+] KB4523204 installed on 11/13/2019
[+] KB4539571 installed on 3/18/2020
[+] KB4549947 installed on 4/15/2020
[+] KB4558997 installed on 7/15/2020
[+] KB4561600 installed on 6/10/2020
[+] KB4562562 installed on 6/10/2020
[+] KB4566424 installed on 8/12/2020
[+] KB4570332 installed on 9/9/2020
[+] KB4570333 installed on 9/9/2020
[*] Post module execution completed

msf6 post(windows/gather/enum_patches) > use post/windows/gather/enum_shares
msf6 post(windows/gather/enum_shares) > run

[*] Running against session 1
[*] No shares were found
[*] Post module execution completed
```

```bash
C:\Temp>powershell.exe -ExecutionPolicy Bypass -File .\jaws.ps1 -OutputFilename JAWS-Enum.txt  
powershell.exe -ExecutionPolicy Bypass -File .\jaws.ps1 -OutputFilename JAWS-Enum.txt

Running J.A.W.S. Enumeration
	- Gathering User Information
	- Gathering Processes, Services and Scheduled Tasks
	- Gathering Installed Software
	- Gathering File System Information
...
```
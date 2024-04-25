# Linux Local Enumeration

## Enumerating System Information

```bash
root@victim-1:~# hostname
hostname
victim-1

root@victim-1:~# cat /etc/issue
cat /etc/issue
Debian GNU/Linux 9 \n \l

root@victim-1:~# cat /etc/*release
cat /etc/*release
PRETTY_NAME="Debian GNU/Linux 9 (stretch)"
NAME="Debian GNU/Linux"
VERSION_ID="9"
VERSION="9 (stretch)"
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

root@victim-1:~# uname -a
uname -a
Linux victim-1 5.4.0-152-generic #169-Ubuntu SMP Tue Jun 6 22:23:09 UTC 2023 x86_64 GNU/Linux

root@victim-1:~# env
env
TZ=UTC-00:00
HOSTNAME=victim-1
PWD=/root
HOME=/root
LAYOUT=en-us-qwerty
SHLVL=1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
_=/usr/bin/env
OLDPWD=/root/vsftpd-2.3.4


root@victim-1:~# lscpu
lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                48
On-line CPU(s) list:   0-47
Thread(s) per core:    1
Core(s) per socket:    48
Socket(s):             1
NUMA node(s):          1
Vendor ID:             AuthenticAMD
CPU family:            25
Model:                 1
Model name:            AMD EPYC 7713 64-Core Processor
Stepping:              1
CPU MHz:               1999.999
BogoMIPS:              3999.99
Hypervisor vendor:     KVM
Virtualization type:   full
L1d cache:             64K
L1i cache:             64K
L2 cache:              512K
L3 cache:              16384K
NUMA node0 CPU(s):     0-47
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm rep_good nopl cpuid extd_apicid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase tsc_adjust bmi1 avx2 smep bmi2 rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr wbnoinvd arat umip pku ospke vaes vpclmulqdq rdpid arch_capabilities


root@victim-1:~# df -h
df -h
Filesystem      Size  Used Avail Use% Mounted on
overlay         1.9T  1.6T  172G  91% /
tmpfs            64M     0   64M   0% /dev
tmpfs            48G     0   48G   0% /sys/fs/cgroup
shm              64M     0   64M   0% /dev/shm
/dev/sda        1.9T  1.6T  172G  91% /etc/hosts
udev             48G     0   48G   0% /dev/tty
tmpfs            48G     0   48G   0% /proc/acpi
tmpfs            48G     0   48G   0% /proc/scsi
tmpfs            48G     0   48G   0% /sys/firmware

root@victim-1:~# lsblk | grep sd
lsblk | grep sd
sda    8:0    0  1.9T  0 disk /etc/hosts
sdb    8:16   0  512M  0 disk [SWAP]


root@victim-1:~# dpkg -l
dpkg -l
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                      Version                    Architecture Description
+++-=========================-==========================-============-===============================================================================
ii  adduser                   3.115                      all          add and remove users and groups
ii  apt                       1.4.8                      i386         commandline package manager
ii  base-files                9.9+deb9u5                 i386         Debian base system miscellaneous files
ii  base-passwd               3.5.43                     i386         Debian base system master password and group files
ii  bash                      4.4-5                      i386         GNU Bourne Again SHell
ii  binutils                  2.28-5                     i386         GNU assembler, linker and binary utilities
ii  bsdutils                  1:2.29.2-1+deb9u1          i386         basic utilities from 4.4BSD-Lite
ii  build-essential           12.3                       i386         Informational list of build-essential packages
ii  bzip2                     1.0.6-8.1                  i386         high-quality block-sorting file compressor - utilities
ii  coreutils                 8.26-3                     i386         GNU core utilities
ii  cpp                       4:6.3.0-4                  i386         GNU C preprocessor (cpp)
ii  cpp-6                     6.3.0-18+deb9u1            i386         GNU C preprocessor
ii  dash                      0.5.8-2.4                  i386         POSIX-compliant shell
ii  debconf                   1.5.61                     all          Debian configuration management system
ii  debian-archive-keyring    2017.5                     all          GnuPG archive keys of the Debian archive
ii  debianutils               4.8.1.1                    i386         Miscellaneous utilities specific to Debian
ii  diffutils                 1:3.5-3                    i386         File comparison utilities
ii  dirmngr                   2.1.18-8~deb9u2            i386         GNU privacy guard - network certificate management service
ii  dpkg                      1.18.25                    i386         Debian package management system
ii  dpkg-dev                  1.18.25                    all          Debian package development tools
ii  e2fslibs:i386             1.43.4-2                   i386         ext2/ext3/ext4 file system libraries
ii  e2fsprogs                 1.43.4-2                   i386         ext2/ext3/ext4 file system utilities
ii  fakeroot                  1.21-3.1                   i386         tool for simulating superuser privileges
ii  findutils                 4.6.0+git+20161106-2       i386         utilities for finding files--find, xargs
ii  g++                       4:6.3.0-4                  i386         GNU C++ compiler
ii  g++-6                     6.3.0-18+deb9u1            i386         GNU C++ compiler
ii  gcc                       4:6.3.0-4                  i386         GNU C compiler
ii  gcc-6                     6.3.0-18+deb9u1            i386         GNU C compiler
ii  gcc-6-base:i386           6.3.0-18+deb9u1            i386         GCC, the GNU Compiler Collection (base package)
ii  gnupg                     2.1.18-8~deb9u2            i386         GNU privacy guard - a free PGP replacement
ii  gnupg-agent               2.1.18-8~deb9u2            i386         GNU privacy guard - cryptographic agent
ii  gnupg-l10n                2.1.18-8~deb9u2            all          GNU privacy guard - localization files
ii  gpgv                      2.1.18-8~deb9u2            i386         GNU privacy guard - signature verification tool
ii  grep                      2.27-2                     i386         GNU grep, egrep and fgrep
ii  gzip                      1.6-5+b1                   i386         GNU compression utilities
ii  hostname                  3.18+b1                    i386         utility to set/show the host name or domain name
ii  init-system-helpers       1.48                       all          helper tools for all init systems
...
```

## Enumerating Users & Groups

```bash
root@victim-1:~/vsftpd-2.3.4# groups root
groups root
root : root


root@victim-1:~/vsftpd-2.3.4# cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/bin/false

root@victim-1:~/vsftpd-2.3.4# last
last

wtmp begins Tue May 17 08:57:26 2022


$ lastlog 
Username         Port     From             Latest
root                                       **Never logged in**
daemon                                     **Never logged in**
bin                                        **Never logged in**
sys                                        **Never logged in**
sync                                       **Never logged in**
games                                      **Never logged in**
man                                        **Never logged in**
lp                                         **Never logged in**
mail                                       **Never logged in**
news                                       **Never logged in**
uucp                                       **Never logged in**
proxy                                      **Never logged in**
www-data                                   **Never logged in**
backup                                     **Never logged in**
list                                       **Never logged in**
```

## Enumerating Network Information

```bash
meterpreter > ifconfig

Interface  1
============
Name         : lo
Hardware MAC : 00:00:00:00:00:00
MTU          : 65536
Flags        : UP,LOOPBACK
IPv4 Address : 127.0.0.1
IPv4 Netmask : 255.0.0.0


Interface  2
============
Name         : ip_vti0
Hardware MAC : 00:00:00:00:00:00
MTU          : 1480
Flags        : NOARP


Interface 346129
============
Name         : eth0
Hardware MAC : 02:42:c0:e0:13:03
MTU          : 1500
Flags        : UP,BROADCAST,MULTICAST
IPv4 Address : 192.224.19.3
IPv4 Netmask : 255.255.255.0


meterpreter > netstat 

Connection list
===============

    Proto  Local address       Remote address      State        User   Inode  PID/Program name
    -----  -------------       --------------      -----        ----   -----  ----------------
    tcp    127.0.0.11:34239    0.0.0.0:*           LISTEN       65534  0      
    tcp    0.0.0.0:21          0.0.0.0:*           LISTEN       0      0      
    tcp    0.0.0.0:6200        0.0.0.0:*           LISTEN       0      0      
    tcp    192.224.19.3:6200   192.224.19.2:41477  ESTABLISHED  0      0      
    tcp    192.224.19.3:21     192.224.19.2:35723  CLOSE_WAIT   0      0      
    tcp    192.224.19.3:56936  192.224.19.2:4433   ESTABLISHED  0      0      
    udp    127.0.0.11:51425    0.0.0.0:*                        65534  0      


meterpreter > route

IPv4 network routes
===================

    Subnet        Netmask        Gateway       Metric  Interface
    ------        -------        -------       ------  ---------
    0.0.0.0       0.0.0.0        192.224.19.1  0       eth0
    192.224.19.0  255.255.255.0  0.0.0.0       0       eth0

No IPv6 routes were found.

meterpreter > arp

ARP cache
=========

    IP address    MAC address        Interface
    ----------    -----------        ---------
    192.224.19.2  02:42:c0:e0:13:02  


```

```bash
root@victim-1:~/vsftpd-2.3.4# ip a s
ip a s
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: ip_vti0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
346129: eth0@if346130: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:c0:e0:13:03 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.224.19.3/24 brd 192.224.19.255 scope global eth0
       valid_lft forever preferred_lft forever

root@victim-1:~/vsftpd-2.3.4# cat /etc/networks
cat /etc/networks
default         0.0.0.0
loopback        127.0.0.0
link-local      169.254.0.0

root@victim-1:~/vsftpd-2.3.4# cat /etc/hostname
cat /etc/hostname
victim-1

root@victim-1:~/vsftpd-2.3.4# cat /etc/hosts
cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
192.224.19.3    victim-1

root@victim-1:~/vsftpd-2.3.4# cat /etc/resolv.conf
cat /etc/resolv.conf
search members.linode.com
nameserver 127.0.0.11
options edns0 trust-ad ndots:0

$ arp -a          
AFi-P-HD-79A3B2.lan (192.168.185.153) at 68:d7:9a:79:a3:b2 [ether] on wlp3s0
amplifi.lan (192.168.185.1) at 6a:d7:9a:73:9e:88 [ether] on wlp3s0
EPSOND2AD80.lan (192.168.185.151) at e0:bb:9e:d2:ad:80 [ether] on wlp3s0
```

## Enumeration Processes & Cron Jobs

```bash
meterpreter > ps

Process List
============

 PID  PPID  Name    Arch    User    Path
 ---  ----  ----    ----    ----    ----
 1    0     sh      x86     root    /bin
 7    1     vsftpd  x86     root    /usr/local/sbin
 8    7     sh      x86     root    /bin
 9    8     vsftpd  x86_64  nobody  .
 18   8     GrBHM   x86_64  root    /tmp


meterpreter > pgrep vsftpd
7
9
```

```bash
$ ps aux --forest
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           2  0.0  0.0      0     0 ?        S    Mar28   0:01 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   Mar28   0:00  \_ [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   Mar28   0:00  \_ [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   Mar28   0:00  \_ [slub_flushwq]
root           6  0.0  0.0      0     0 ?        I<   Mar28   0:00  \_ [netns]
root          11  0.0  0.0      0     0 ?        I<   Mar28   0:00  \_ [mm_percpu_wq]
root          12  0.0  0.0      0     0 ?        I    Mar28   0:00  \_ [rcu_tasks_kthread]
root          13  0.0  0.0      0     0 ?        I    Mar28   0:00  \_ [rcu_tasks_rude_kthread]
root          14  0.0  0.0      0     0 ?        I    Mar28   0:00  \_ [rcu_tasks_trace_kthread]
root          15  0.0  0.0      0     0 ?        S    Mar28   0:18  \_ [ksoftirqd/0]
root          16  0.0  0.0      0     0 ?        I    Mar28   7:42  \_ [rcu_preempt]
root          17  0.0  0.0      0     0 ?        S    Mar28   0:02  \_ [migration/0]


$ top

$ crontab -l                                      
no crontab for ehogue

root@victim-1:~/vsftpd-2.3.4# ls -la /etc/cron*
ls -la /etc/cron*
total 20
drwxr-xr-x 2 root root 4096 Oct 11  2018 .
drwxr-xr-x 1 root root 4096 Apr  4 10:16 ..
-rwxr-xr-x 1 root root 1474 Sep 13  2017 apt-compat
-rwxr-xr-x 1 root root 1597 Jun 26  2018 dpkg
-rwxr-xr-x 1 root root  249 May 17  2017 passwd
```

## Automating Linux Local Enumeration

[LinEnum](https://github.com/rebootuser/LinEnum)

```bash
msf5 exploit(multi/http/apache_mod_cgi_bash_env_exec) > use post/linux/gather/enum_configs
msf5 post(linux/gather/enum_configs) > options

Module options (post/linux/gather/enum_configs):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION                   yes       The session to run this module on.

msf5 post(linux/gather/enum_configs) > setg SESSION 1
SESSION => 1

msf5 post(linux/gather/enum_configs) > run

[*] Running module against 192.247.177.3 [victim-1]
[*] Info:
[*] 	Ubuntu 14.04.6 LTS  
[*] 	Linux victim-1 5.4.0-152-generic #169-Ubuntu SMP Tue Jun 6 22:23:09 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
[-] Failed to open file: /etc/apache2/apache2.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/apache2/ports.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/nginx/nginx.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/snort/snort.conf: core_channel_open: Operation failed: 1
[+] my.cnf stored in /root/.msf4/loot/20240404173658_default_192.247.177.3_linux.enum.conf_589394.txt
[-] Failed to open file: /etc/ufw/ufw.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/ufw/sysctl.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/security.access.conf: core_channel_open: Operation failed: 1
[+] shells stored in /root/.msf4/loot/20240404173658_default_192.247.177.3_linux.enum.conf_931554.txt
[+] sepermit.conf stored in /root/.msf4/loot/20240404173658_default_192.247.177.3_linux.enum.conf_129044.txt
[+] ca-certificates.conf stored in /root/.msf4/loot/20240404173658_default_192.247.177.3_linux.enum.conf_629434.txt
[+] access.conf stored in /root/.msf4/loot/20240404173658_default_192.247.177.3_linux.enum.conf_981562.txt
[-] Failed to open file: /etc/gated.conf: core_channel_open: Operation failed: 1
[+] rpc stored in /root/.msf4/loot/20240404173658_default_192.247.177.3_linux.enum.conf_294517.txt
[-] Failed to open file: /etc/psad/psad.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/mysql/debian.cnf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/chkrootkit.conf: core_channel_open: Operation failed: 1
[+] logrotate.conf stored in /root/.msf4/loot/20240404173658_default_192.247.177.3_linux.enum.conf_621104.txt
[-] Failed to open file: /etc/rkhunter.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/samba/smb.conf: core_channel_open: Operation failed: 1
[+] ldap.conf stored in /root/.msf4/loot/20240404173658_default_192.247.177.3_linux.enum.conf_534115.txt
[-] Failed to open file: /etc/openldap/openldap.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/cups/cups.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/opt/lampp/etc/httpd.conf: core_channel_open: Operation failed: 1
[+] sysctl.conf stored in /root/.msf4/loot/20240404173658_default_192.247.177.3_linux.enum.conf_363076.txt
[-] Failed to open file: /etc/proxychains.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/cups/snmp.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/mail/sendmail.conf: core_channel_open: Operation failed: 1
[-] Failed to open file: /etc/snmp/snmp.conf: core_channel_open: Operation failed: 1
[*] Post module execution completed

msf5 post(linux/gather/enum_configs) > use post/linux/gather/enum_network
msf5 post(linux/gather/enum_network) > run

[*] Running module against 192.247.177.3
[*] Module running as daemon
[+] Info:
[+] 	Ubuntu 14.04.6 LTS  
[+] 	Linux victim-1 5.4.0-152-generic #169-Ubuntu SMP Tue Jun 6 22:23:09 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
[*] Collecting data...
[-] Failed to open file: /etc/ssh/sshd_config: core_channel_open: Operation failed: 1
[+] Network config stored in /root/.msf4/loot/20240404173842_default_192.247.177.3_linux.enum.netwo_180462.txt
[+] Route table stored in /root/.msf4/loot/20240404173842_default_192.247.177.3_linux.enum.netwo_289364.txt
[-] Unable to get data for Firewall config
[+] DNS config stored in /root/.msf4/loot/20240404173842_default_192.247.177.3_linux.enum.netwo_790331.txt
[-] Unable to get data for SSHD config
[+] Host file stored in /root/.msf4/loot/20240404173842_default_192.247.177.3_linux.enum.netwo_776608.txt
[-] Unable to get data for Active connections
[-] Unable to get data for Wireless information
[+] Listening ports stored in /root/.msf4/loot/20240404173842_default_192.247.177.3_linux.enum.netwo_209168.txt
[+] If-Up/If-Down stored in /root/.msf4/loot/20240404173842_default_192.247.177.3_linux.enum.netwo_510915.txt
[*] Post module execution completed


msf5 post(linux/gather/enum_network) > use post/linux/gather/enum_system
msf5 post(linux/gather/enum_system) > run

[+] Info:
[+] 	Ubuntu 14.04.6 LTS  
[+] 	Linux victim-1 5.4.0-152-generic #169-Ubuntu SMP Tue Jun 6 22:23:09 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
[+] 	Module running as "daemon" user
[*] Linux version stored in /root/.msf4/loot/20240404174055_default_192.247.177.3_linux.enum.syste_736377.txt
[*] User accounts stored in /root/.msf4/loot/20240404174055_default_192.247.177.3_linux.enum.syste_415841.txt
[*] Installed Packages stored in /root/.msf4/loot/20240404174055_default_192.247.177.3_linux.enum.syste_180880.txt
[*] Running Services stored in /root/.msf4/loot/20240404174055_default_192.247.177.3_linux.enum.syste_928238.txt
[*] Cron jobs stored in /root/.msf4/loot/20240404174055_default_192.247.177.3_linux.enum.syste_137666.txt
[*] Disk info stored in /root/.msf4/loot/20240404174055_default_192.247.177.3_linux.enum.syste_845459.txt
[*] Logfiles stored in /root/.msf4/loot/20240404174055_default_192.247.177.3_linux.enum.syste_485264.txt
[*] Setuid/setgid files stored in /root/.msf4/loot/20240404174055_default_192.247.177.3_linux.enum.syste_530109.txt


msf5 post(linux/gather/enum_system) > use post/linux/gather/checkvm
msf5 post(linux/gather/checkvm) > run

[*] Gathering System info ....
[+] This appears to be a 'Qemu/KVM' virtual machine
[*] Post module execution completed
```
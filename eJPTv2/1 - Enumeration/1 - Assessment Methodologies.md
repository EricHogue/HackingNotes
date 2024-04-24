
# Section 1 - Assessment Methodologies

## Tools

### DNS

```bash
$ host erichogue.ca
erichogue.ca has address 185.199.111.153
erichogue.ca has address 185.199.109.153
erichogue.ca has address 185.199.108.153
erichogue.ca has address 185.199.110.153
erichogue.ca mail is handled by 5 alt1.aspmx.l.google.com.
erichogue.ca mail is handled by 10 aspmx3.googlemail.com.
erichogue.ca mail is handled by 5 alt2.aspmx.l.google.com.
erichogue.ca mail is handled by 1 aspmx.l.google.com.
erichogue.ca mail is handled by 10 aspmx2.googlemail.com.
```

```bash
 whois erichogue.ca
Domain Name: erichogue.ca
Registry Domain ID: D1019462-CIRA
Registrar WHOIS Server: whois.ca.fury.ca
Registrar URL: https://www.namecheap.com/
Updated Date: 2023-06-13T06:46:43Z
Creation Date: 2009-07-14T00:45:12Z
Registry Expiry Date: 2024-07-13T04:00:00Z
Registrar: Go Get Canada Domain Registrar Ltd.
Registrar IANA ID: not applicable
Registrar Abuse Contact Email: abuse@namecheap.com
Registrar Abuse Contact Phone: +1.6613102107
Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
Registry Registrant ID: REDACTED FOR PRIVACY
```


```bash
$ dnsrecon -d erichogue.ca
[*] std: Performing General Enumeration against: erichogue.ca...
[-] All nameservers failed to answer the DNSSEC query for erichogue.ca
[*]      SOA dns1.registrar-servers.com 156.154.132.200
[*]      SOA dns1.registrar-servers.com 2610:a1:1024::200
[*]      NS dns1.registrar-servers.com 156.154.132.200
[*]      Bind Version for 156.154.132.200 Nameserver"
[*]      NS dns1.registrar-servers.com 2610:a1:1024::200
[*]      NS dns2.registrar-servers.com 156.154.133.200
[*]      Bind Version for 156.154.133.200 Nameserver"
[*]      NS dns2.registrar-servers.com 2610:a1:1025::200
[*]      MX aspmx2.googlemail.com 209.85.202.26
[*]      MX aspmx3.googlemail.com 64.233.184.27
[*]      MX alt1.aspmx.l.google.com 209.85.202.27
[*]      MX alt2.aspmx.l.google.com 64.233.184.27
[*]      MX aspmx.l.google.com 172.253.115.27
[*]      MX aspmx2.googlemail.com 2a00:1450:400b:c00::1b
[*]      MX aspmx3.googlemail.com 2a00:1450:400c:c0b::1a
[*]      MX alt1.aspmx.l.google.com 2a00:1450:400b:c00::1a
[*]      MX alt2.aspmx.l.google.com 2a00:1450:400c:c0b::1b
[*]      MX aspmx.l.google.com 2607:f8b0:4004:c09::1b
[*]      A erichogue.ca 185.199.109.153
[*]      A erichogue.ca 185.199.108.153
[*]      A erichogue.ca 185.199.110.153
[*]      A erichogue.ca 185.199.111.153
[*] Enumerating SRV Records
[-] No SRV Records Found for erichogue.ca
```

https://dnsdumpster.com/

#### Find Sub Domains

```bash
$ sublist3r -d erichogue.ca

                 ____        _     _ _     _   _____
                / ___| _   _| |__ | (_)___| |_|___ / _ __
                \___ \| | | | '_ \| | / __| __| |_ \| '__|
                 ___) | |_| | |_) | | \__ \ |_ ___) | |
                |____/ \__,_|_.__/|_|_|___/\__|____/|_|

                # Coded By Ahmed Aboul-Ela - @aboul3la

[-] Enumerating subdomains now for erichogue.ca
[-] Searching now in Baidu..
[-] Searching now in Yahoo..
[-] Searching now in Google..
[-] Searching now in Bing..
[-] Searching now in Ask..
[-] Searching now in Netcraft..
[-] Searching now in DNSdumpster..
[-] Searching now in Virustotal..
[-] Searching now in ThreatCrowd..
[-] Searching now in SSL Certificates..
[-] Searching now in PassiveDNS..
[!] Error: Virustotal probably now is blocking our requests
[-] Total Unique Subdomains Found: 2
www.erichogue.ca
s.erichogue.ca
```

Find subdomains, emails, IPs, ...

```bash
$ theHarvester -d "erichogue.ca" -ball
Read proxies.yaml from /home/ehogue/.theHarvester/proxies.yaml
*******************************************************************
*  _   _                                            _             *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
* | __|  _ \ / _ \  / /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__| *
* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\__ \ ||  __/ |    *
*  \__|_| |_|\___| \/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|    *
*                                                                 *
* theHarvester 4.5.0                                              *
* Coded by Christian Martorella                                   *
* Edge-Security Research                                          *
* cmartorella@edge-security.com                                   *
*                                                                 *
*******************************************************************

[*] Target: erichogue.ca

Read api-keys.yaml from /etc/theHarvester/api-keys.yaml

...

[!] Missing API key for zoomeye.
[*] Searching Anubis.
        Searching 0 results.
[*] Searching Bing.

[*] Searching Baidu.
An exception has occurred: 400, message:
  Can not decode content-encoding: br
        Searching results.
[*] Searching Certspotter.
[*] Searching CRTsh.
[*] Searching Dnsdumpster.
[*] Searching Hackertarget.
[*] Searching Duckduckgo.
[*] Searching Otx.
[*] Searching Rapiddns.

...

An exception has occurred: 400, message:
  Can not decode content-encoding: br
[*] Searching Brave.

[*] LinkedIn Links found: 0
---------------------

[*] IPs found: 7
-------------------
104.28.16.11
104.28.17.11
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
192.241.144.62

[*] Emails found: 0
----------------------

[*] Hosts found: 1
---------------------
s.erichogue.ca
```
#### DNS Zone Transfer

If works, will provide lots of information 

```bash
$ dnsenum zonetransfer.me
dnsenum VERSION:1.2.6

-----   zonetransfer.me   -----


Host's addresses:
__________________

zonetransfer.me.                         60       IN    A        5.196.105.14


Name Servers:
______________

nsztm1.digi.ninja.                       60       IN    A        81.4.108.41
nsztm2.digi.ninja.                       60       IN    A        34.225.33.2


Mail (MX) Servers:
___________________

ASPMX.L.GOOGLE.COM.                      60       IN    A        142.251.163.27
ASPMX4.GOOGLEMAIL.COM.                   60       IN    A        142.250.27.27
ASPMX2.GOOGLEMAIL.COM.                   60       IN    A        209.85.202.26
ASPMX3.GOOGLEMAIL.COM.                   60       IN    A        64.233.184.26
ALT2.ASPMX.L.GOOGLE.COM.                 60       IN    A        64.233.184.27
ASPMX5.GOOGLEMAIL.COM.                   60       IN    A        142.250.153.26
ALT1.ASPMX.L.GOOGLE.COM.                 37       IN    A        209.85.202.26


Trying Zone Transfers and getting Bind Versions:
_________________________________________________


Trying Zone Transfer for zonetransfer.me on nsztm1.digi.ninja ...
zonetransfer.me.                         7200     IN    SOA               (
zonetransfer.me.                         300      IN    HINFO        "Casio
zonetransfer.me.                         301      IN    TXT               (
...
zonetransfer.me.                         7200     IN    MX                0
zonetransfer.me.                         7200     IN    MX               20
zonetransfer.me.                         7200     IN    A        5.196.105.14
zonetransfer.me.                         7200     IN    NS       nsztm1.digi.ninja.
zonetransfer.me.                         7200     IN    NS       nsztm2.digi.ninja.
_acme-challenge.zonetransfer.me.         301      IN    TXT               (
_sip._tcp.zonetransfer.me.               14000    IN    SRV               0
14.105.196.5.IN-ADDR.ARPA.zonetransfer.me. 7200     IN    PTR      www.zonetransfer.me.
asfdbauthdns.zonetransfer.me.            7900     IN    AFSDB             1
asfdbbox.zonetransfer.me.                7200     IN    A         127.0.0.1
asfdbvolume.zonetransfer.me.             7800     IN    AFSDB             1
canberra-office.zonetransfer.me.         7200     IN    A        202.14.81.230
cmdexec.zonetransfer.me.                 300      IN    TXT              ";
contact.zonetransfer.me.                 2592000  IN    TXT               (
dc-office.zonetransfer.me.               7200     IN    A        143.228.181.132
deadbeef.zonetransfer.me.                7201     IN    AAAA     dead:beaf::
dr.zonetransfer.me.                      300      IN    LOC              53
DZC.zonetransfer.me.                     7200     IN    TXT         AbCdEfG
email.zonetransfer.me.                   2222     IN    NAPTR             (
email.zonetransfer.me.                   7200     IN    A        74.125.206.26
Hello.zonetransfer.me.                   7200     IN    TXT             "Hi
home.zonetransfer.me.                    7200     IN    A         127.0.0.1
Info.zonetransfer.me.                    7200     IN    TXT               (
internal.zonetransfer.me.                300      IN    NS       intns1.zonetransfer.me.
internal.zonetransfer.me.                300      IN    NS       intns2.zonetransfer.me.
intns1.zonetransfer.me.                  300      IN    A        81.4.108.41
intns2.zonetransfer.me.                  300      IN    A        167.88.42.94
office.zonetransfer.me.                  7200     IN    A        4.23.39.254
ipv6actnow.org.zonetransfer.me.          7200     IN    AAAA     2001:67c:2e8:11::c100:1332
owa.zonetransfer.me.                     7200     IN    A        207.46.197.32
robinwood.zonetransfer.me.               302      IN    TXT          "Robin
rp.zonetransfer.me.                      321      IN    RP                (
sip.zonetransfer.me.                     3333     IN    NAPTR             (
sqli.zonetransfer.me.                    300      IN    TXT              "'
sshock.zonetransfer.me.                  7200     IN    TXT             "()
staging.zonetransfer.me.                 7200     IN    CNAME    www.sydneyoperahouse.com.
alltcpportsopen.firewall.test.zonetransfer.me. 301      IN    A         127.0.0.1
testing.zonetransfer.me.                 301      IN    CNAME    www.zonetransfer.me.
vpn.zonetransfer.me.                     4000     IN    A        174.36.59.154
www.zonetransfer.me.                     7200     IN    A        5.196.105.14
xss.zonetransfer.me.                     300      IN    TXT      "'><script>alert('Boo')</script>"

Trying Zone Transfer for zonetransfer.me on nsztm2.digi.ninja ...
zonetransfer.me.                         7200     IN    SOA               (
zonetransfer.me.                         300      IN    HINFO        "Casio
zonetransfer.me.                         301      IN    TXT               (
...
zonetransfer.me.                         7200     IN    NS       nsztm2.digi.ninja.
_acme-challenge.zonetransfer.me.         301      IN    TXT               (
_acme-challenge.zonetransfer.me.         301      IN    TXT               (
_sip._tcp.zonetransfer.me.               14000    IN    SRV               0
14.105.196.5.IN-ADDR.ARPA.zonetransfer.me. 7200     IN    PTR      www.zonetransfer.me.
asfdbauthdns.zonetransfer.me.            7900     IN    AFSDB             1
asfdbbox.zonetransfer.me.                7200     IN    A         127.0.0.1
asfdbvolume.zonetransfer.me.             7800     IN    AFSDB             1
canberra-office.zonetransfer.me.         7200     IN    A        202.14.81.230
cmdexec.zonetransfer.me.                 300      IN    TXT              ";
contact.zonetransfer.me.                 2592000  IN    TXT               (
dc-office.zonetransfer.me.               7200     IN    A        143.228.181.132
deadbeef.zonetransfer.me.                7201     IN    AAAA     dead:beaf::
dr.zonetransfer.me.                      300      IN    LOC              53
DZC.zonetransfer.me.                     7200     IN    TXT         AbCdEfG
email.zonetransfer.me.                   2222     IN    NAPTR             (
email.zonetransfer.me.                   7200     IN    A        74.125.206.26
Hello.zonetransfer.me.                   7200     IN    TXT             "Hi
home.zonetransfer.me.                    7200     IN    A         127.0.0.1
Info.zonetransfer.me.                    7200     IN    TXT               (
internal.zonetransfer.me.                300      IN    NS       intns1.zonetransfer.me.
internal.zonetransfer.me.                300      IN    NS       intns2.zonetransfer.me.
intns1.zonetransfer.me.                  300      IN    A        81.4.108.41
intns2.zonetransfer.me.                  300      IN    A        52.91.28.78
office.zonetransfer.me.                  7200     IN    A        4.23.39.254
ipv6actnow.org.zonetransfer.me.          7200     IN    AAAA     2001:67c:2e8:11::c100:1332
owa.zonetransfer.me.                     7200     IN    A        207.46.197.32
robinwood.zonetransfer.me.               302      IN    TXT          "Robin
rp.zonetransfer.me.                      321      IN    RP                (
sip.zonetransfer.me.                     3333     IN    NAPTR             (
sqli.zonetransfer.me.                    300      IN    TXT              "'
sshock.zonetransfer.me.                  7200     IN    TXT             "()
staging.zonetransfer.me.                 7200     IN    CNAME    www.sydneyoperahouse.com.
alltcpportsopen.firewall.test.zonetransfer.me. 301      IN    A         127.0.0.1
testing.zonetransfer.me.                 301      IN    CNAME    www.zonetransfer.me.
vpn.zonetransfer.me.                     4000     IN    A        174.36.59.154
www.zonetransfer.me.                     7200     IN    A        5.196.105.14
xss.zonetransfer.me.                     300      IN    TXT      "'><script>alert('Boo')</script>"


Brute forcing with /usr/share/dnsenum/dns.txt:
_______________________________________________
```

```bash
$ dig axfr @dns1.registrar-servers.com erichogue.ca

; <<>> DiG 9.19.19-1-Debian <<>> axfr @dns1.registrar-servers.com erichogue.ca
; (2 servers found)
;; global options: +cmd
; Transfer failed.
```

### Google Dorking

* Limit to domain: `site:erichogue.ca`
    * Includes subdomains
* `inurl:`
* `intitle:`
    * Find directory listing: `intitle:index of`
* `filetype:pdf`
* Find older version `cache:erichogue.ca`
* Some creds: `inurl:auth_user_file.txt`
* [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)

## Network Scans

### nmap Ping scan

```bash
$ sudo nmap -sn 192.168.185.118/24
Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-12 18:21 EST
Nmap scan report for router (192.168.185.1)
Host is up (0.058s latency).
...

Nmap done: 256 IP addresses (7 hosts up) scanned in 2.85 seconds
```

Force normal ping scan on local network. Without this, it only do arp requests

```bash
root@attackdefense:~# nmap -sn 10.10.4.0/24 --send-ip
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-14 02:39 IST
Nmap scan report for linux (10.10.4.1)
Host is up (0.00021s latency).
MAC Address: 02:42:D1:6D:23:52 (Unknown)
Nmap scan report for attackdefense.com (10.10.4.2)
Host is up.
Nmap done: 256 IP addresses (2 hosts up) scanned in 17.56 seconds
```

### Ping Sweep
```bash
root@attackdefense:~# ping -c1 -b 10.1.0.0
WARNING: pinging broadcast address
PING 10.1.0.0 (10.1.0.0) 56(84) bytes of data.

--- 10.1.0.0 ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms
```

## Machine Scans

Host discorver, SYN scan
Send a syn, get the syn/ack, reply with rst

```bash
root@attackdefense:~# nmap -sn 10.4.23.83
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-14 02:51 IST
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.10 seconds

root@attackdefense:~# nmap -sn -PS 10.4.23.83
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-14 02:51 IST
Nmap scan report for 10.4.23.83
Host is up (0.0085s latency).
Nmap done: 1 IP address (1 host up) scanned in 0.10 seconds

# use ports 1 to 1000
root@attackdefense:~# nmap -sn -PS1-1000 10.4.23.83
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-14 02:55 IST
Nmap scan report for 10.4.23.83
Host is up (0.0080s latency).
Nmap done: 1 IP address (1 host up) scanned in 17.55 seconds
```

ACK scan
Sends only an ack, expect a reset

Windows Firewall blocks this one

```bash
root@attackdefense:~# nmap -sn -PA 10.4.18.64
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-14 03:02 IST
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 2.11 seconds

root@attackdefense:~# nmap -sn -PA1-1000 10.4.18.64
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-14 03:03 IST
Stats: 0:00:34 elapsed; 0 hosts completed (0 up), 1 undergoing Ping Scan
Ping Scan Timing: About 16.50% done; ETC: 03:06 (0:02:52 remaining)
Stats: 0:01:27 elapsed; 0 hosts completed (0 up), 1 undergoing Ping Scan
Ping Scan Timing: About 43.00% done; ETC: 03:06 (0:01:55 remaining)
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 201.30 seconds
```

Instructor methodology


```bash
root@attackdefense:~# nmap -sn -v -T4 10.4.18.64
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-14 03:09 IST
Initiating Ping Scan at 03:09
Scanning 10.4.18.64 [4 ports]
Completed Ping Scan at 03:09, 2.06s elapsed (1 total hosts)
Nmap scan report for 10.4.18.64 [host down]
Read data files from: /usr/bin/../share/nmap
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 2.11 seconds
           Raw packets sent: 8 (304B) | Rcvd: 0 (0B)


root@attackdefense:~# nmap -sn -PS21,22,25,80,443,445,3389,8080 -v -T4 10.4.18.64
Starting Nmap 7.70 ( https://nmap.org ) at 2024-01-14 03:11 IST
Initiating Ping Scan at 03:11
Scanning 10.4.18.64 [8 ports]
Completed Ping Scan at 03:11, 0.06s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 03:11
Completed Parallel DNS resolution of 1 host. at 03:11, 0.00s elapsed
Nmap scan report for 10.4.18.64
Host is up (0.0094s latency).
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.10 seconds
           Raw packets sent: 8 (352B) | Rcvd: 1 (44B)


## Check Opend TCP Connections

```bash
$ netstat -antp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:35593         0.0.0.0:*               LISTEN      -
tcp        0      0 10.0.2.6:34386          142.251.33.163:80       ESTABLISHED 18450/firefox-esr
tcp        0      0 10.0.2.6:46554          13.33.3.217:80          ESTABLISHED 18450/firefox-esr
tcp        0      0 10.0.2.6:58394          34.117.237.239:443      ESTABLISHED 18450/firefox-esr
tcp        0    415 10.0.2.6:54922          184.150.163.56:80       ESTABLISHED 18450/firefox-esr
tcp        0      0 10.0.2.6:44000          3.214.112.20:443        ESTABLISHED 18450/firefox-esr
tcp        0      0 10.0.2.6:45090          34.107.243.93:443       ESTABLISHED 18450/firefox-esr
tcp        0    415 10.0.2.6:54914          184.150.163.56:80       ESTABLISHED 18450/firefox-esr
tcp        0      0 10.0.2.6:50320          142.251.41.74:443       TIME_WAIT   -
tcp        0      0 10.0.2.6:43856          34.120.115.102:443      ESTABLISHED 18450/firefox-esr
tcp        0      0 10.0.2.6:46030          34.160.144.191:443      ESTABLISHED 18450/firefox-esr
tcp        0      0 10.0.2.6:45076          34.107.243.93:443       ESTABLISHED 18450/firefox-esr
tcp        0      0 10.0.2.6:43850          34.120.115.102:443      ESTABLISHED 18450/firefox-esr
```
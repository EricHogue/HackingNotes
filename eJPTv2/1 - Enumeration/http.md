# HTTP

## Detect Used Technologies

```bash
root@attackdefense:~# whatweb $target
Ignoring eventmachine-1.3.0.dev.1 because its extensions are not built. Try: gem pristine eventmachine --version 1.3.0.dev.1
Ignoring fxruby-1.6.29 because its extensions are not built. Try: gem pristine fxruby --version 1.6.29
http://10.4.21.24 [302 Found] ASP_NET[4.0.30319], Cookies[ASP.NET_SessionId,Server], Country[RESERVED][ZZ], HTTPServer[Microsoft-IIS/10.0], HttpOnly[ASP.NET_SessionId], IP[10.4.21.24], Microsoft-IIS[10.0], RedirectLocation[/Default.aspx], Title[Object moved], X-Powered-By[ASP.NET], X-XSS-Protection[0]
http://10.4.21.24/Default.aspx [302 Found] ASP_NET[4.0.30319], Cookies[ASP.NET_SessionId,Server], Country[RESERVED][ZZ], HTTPServer[Microsoft-IIS/10.0], HttpOnly[ASP.NET_SessionId], IP[10.4.21.24], Microsoft-IIS[10.0], RedirectLocation[/Default.aspx], Title[Object moved], X-Powered-By[ASP.NET], X-XSS-Protection[0]
```

```bash
$ whatweb https://erichogue.ca
https://erichogue.ca [200 OK] Email[blog@erichogue.ca], HTML5, HTTPServer[GitHub.com], IP[185.199.110.153], Open-Graph-Protocol, Title[Eric Hogue's Blog], UncommonHeaders[access-control-allow-origin,x-proxy-cache,x-github-request-id,x-served-by,x-cache-hits,x-timer,x-fastly-request-id], Via-Proxy[1.1 varnish], X-UA-Compatible[IE=edge]
```

* [HTTrack](https://www.httrack.com/) - Download webiste
* https://sitereport.netcraft.com/?url=https%3A%2F%2Ferichogue.ca

### Identify WAF

```bash
$ wafw00f https://erichogue.ca

                   ______
                  /      \
                 (  Woof! )
                  \  ____/                      )
                  ,,                           ) (_
             .-. -    _______                 ( |__|
            ()``; |==|_______)                .)|__|
            / ('        /|\                  (  |__|
        (  /  )        / | \                  . |__|
         \(_)_))      /  |  \                   |__|

                    ~ WAFW00F : v2.2.0 ~
    The Web Application Firewall Fingerprinting Toolkit

[*] Checking https://erichogue.ca
[+] The site https://erichogue.ca is behind Fastly (Fastly CDN) WAF.
[~] Number of requests: 2
```

## Directories/Files Brute Force

```bash
$ dirb http://192.75.246.3

$ gobuster dir --url http://192.75.246.3 --wordlist /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-words.txt -e
```

```bash
root@attackdefense:~# nmap $target -p 80 -script http-enum
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-17 17:57 IST
Nmap scan report for 10.4.25.204
Host is up (0.0080s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-enum:
|   /content/: Potentially interesting folder
|   /downloads/: Potentially interesting folder
|_  /webdav/: Potentially interesting folder

Nmap done: 1 IP address (1 host up) scanned in 24.77 seconds
```

```bash
msf6 > use auxiliary/scanner/http/brute_dirs

msf6 auxiliary(scanner/http/brute_dirs) > options

Module options (auxiliary/scanner/http/brute_dirs):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   DELAY    0                yes       The delay between connections, per thread, in milliseconds
   FORMAT   a,aa,aaa         yes       The expected directory format (a alpha, d digit, A upperalpha)
   JITTER   0                yes       The delay jitter factor (maximum value by which to +/- DELAY) in milliseconds.
   PATH     /                yes       The path to identify directories
   Proxies                   no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                    yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT    80               yes       The target port (TCP)
   SSL      false            no        Negotiate SSL/TLS for outgoing connections
   THREADS  1                yes       The number of concurrent threads (max one per host)
   TIMEOUT  20               yes       The socket connect/read timeout in seconds
   VHOST                     no        HTTP server virtual host

msf6 auxiliary(scanner/http/brute_dirs) > set RHOSTS 192.128.212.3
RHOSTS => 192.128.212.3

msf6 auxiliary(scanner/http/brute_dirs) > exploit

[*] Using code '404' as not found.
[+] Found http://192.128.212.3:80/dir/ 200
[+] Found http://192.128.212.3:80/src/ 200
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/http/brute_dirs) >
```

## Supported Methods

```bash
root@attackdefense:~# nmap $target -p 80 -script http-methods --script-args http-methods.url=/webdav/
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-17 18:00 IST
Nmap scan report for 10.4.25.204
Host is up (0.0080s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-methods:
|   Supported Methods: OPTIONS TRACE GET HEAD POST COPY PROPFIND LOCK UNLOCK PROPPATCH MKCOL PUT DELETE MOVE
|_  Potentially risky methods: TRACE COPY PROPFIND LOCK UNLOCK PROPPATCH MKCOL PUT DELETE MOVE

Nmap done: 1 IP address (1 host up) scanned in 0.51 seconds
```

## Webdav

```bash
root@attackdefense:~# nmap $target -p 80 -script http-webdav-scan --script-args http-methods.url=/webdav/
Starting Nmap 7.91 ( https://nmap.org ) at 2024-01-17 18:01 IST
Nmap scan report for 10.4.25.204
Host is up (0.0080s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-webdav-scan:
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, POST, COPY, PROPFIND, LOCK, UNLOCK
|   Public Options: OPTIONS, TRACE, GET, HEAD, POST, PROPFIND, PROPPATCH, MKCOL, PUT, DELETE, COPY, MOVE, LOCK, UNLOCK
|   Server Type: Microsoft-IIS/10.0
|   WebDAV type: Unknown
|_  Server Date: Wed, 17 Jan 2024 12:31:46 GMT

Nmap done: 1 IP address (1 host up) scanned in 0.44 seconds
```

## HTTP Versions

```bash
msf6 > use auxiliary/scanner/http/http_version

msf6 auxiliary(scanner/http/http_version) > options

Module options (auxiliary/scanner/http/http_version):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   Proxies                   no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                    yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT    80               yes       The target port (TCP)
   SSL      false            no        Negotiate SSL/TLS for outgoing connections
   THREADS  1                yes       The number of concurrent threads (max one per host)
   VHOST                     no        HTTP server virtual host

msf6 auxiliary(scanner/http/http_version) > set RHOSTS 192.128.212.3
RHOSTS => 192.128.212.3

msf6 auxiliary(scanner/http/http_version) > exploit

[+] 192.128.212.3:80 Apache/2.4.18 (Ubuntu)
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

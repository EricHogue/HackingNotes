# Resources

* GTFOBins - https://gtfobins.github.io/
* Payloads All The Things - https://github.com/swisskyrepo/PayloadsAllTheThings


## Enumerations 

### Basic Scan

* Agressive scan - Will perform OS detection and version detection
    * `nmap -A -oN nmap.txt $IP`
* Run vulnerabilities scripts
    * `nmap -script vuln -oN nmapVuln.txt $IP`
* Scann all the ports
    * `nmap -A -p- -oN nmapFull.txt $IP`

### Enumerate Web Site Folders

* `gobuster dir -e -u http://$IP/ -t30 -w /usr/share/dirb/wordlists/common.txt  | tee gobuster.txt`
* `gobuster dir -e -u http://$IP/ -t30 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt  | tee gobuster2.txt`
* `wfuzz -c -z file,/usr/share/wordlists/dirb/big.txt --hw 54 -t10 "$IP/FUZZ"`

### Find SubDomains
* `wfuzz -c -w /usr/share/amass/wordlists/subdomains-top1mil-5000.txt -t30 --hw 290 -H "Host:FUZZ.somedomain.com" "http://somedomain.com/"`

### Enumerate SMB
* `enum4linux -a IP | tee enum4linux.txt`
* `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse -oN nmapSamba.txt IP`
* `smbmap -H IP`
* `smbclient -U guest \\\\10.10.166.254\\IPC$`

### Enumerate Mounts
* `nmap -p PORT --script=nfs-ls,nfs-statfs,nfs-showmount -oN nmapRpc.txt IP`
    * To mount: `sudo mount -t nfs $IP:$SOURCE_PATH $DESTINATION_PATH`
* `showmount -e $IP`

### Enumerate Wordpress Site
* Get users: `wpscan --url $URL -e vp,u`


## Brute Forcing

### Brute Force Web Site Password
* `hydra -l SomeUser -P /usr/share/wordlists/rockyou.txt -f -u -e snr -t64 -m '/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^:incorrect' IP http-post-form`
* Basic auth: `hydra -L users.txt -P /usr/share/wordlists/rockyou.txt -f -e snr -u -t64 10.10.174.130 http-head`
* Combine wordlists: `/usr/lib/hashcat-utils/combinator.bin colors.txt numbers.txt > wordlist.txt`

#### Wordpress
* `hydra -l wade -P /usr/share/wordlists/rockyou.txt -u -f -t64 -m '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=%2Fretro%2Fwp-admin%2F&testcookie=1:S=Location' $URL http-post-form -v -e snr`
* `wpscan --url $URL --usernames admin --passwords /usr/share/wordlists/rockyou.txt --max-threads 50`

### SSH
* `hydra -l root -P /usr/share/wordlists/rockyou.txt -f -u -e snr -t32 $IP ssh`

### SMB
`hydra -l fox -P /usr/share/wordlists/rockyou.txt -u -e snr $IP smb`

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

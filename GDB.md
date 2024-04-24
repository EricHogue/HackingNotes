
## Documentation
* [Debugging with GDB](https://sourceware.org/gdb/current/onlinedocs/gdb.html/)
    * [Single Page](https://sourceware.org/gdb/current/onlinedocs/gdb)
    * [PDF](https://sourceware.org/gdb/current/onlinedocs/gdb.pdf)

## Config

in ~/.gdbinit

```bash
set history save on
set disassembly-flavor intel
set disassemble-next-line on

unset env LINES
unset env COLUMNS
```

## Commands

| Command | Description | Example |
|------|-------|------|
| r / run | Run the program | |
| c / continue | Continue the execution | |
| b / break | Add a breakpoint | b * main + 10 |
| info breakpoints | Show breakpoints | |
| info functions | List the functions | |
| disas / disasemble | Show disasembled code | disas main |
| p / print | print a value | p $rax |
| info registers | Show the registers and their value | |
| find | Search the memory | find 0x41414141 (find a bunch of As) |
| x | Examine the memory at a location | x/s $rax (Shows the string at rax) |



## Running

* Use file content
    * `run < /tmp/somefile`
* Sending stdin data in GDB
    * `run < <(python -c "print 'A' * 40 + '\xef\xbe\xad\xde'")`
* Sending address without needing to convert to little endian first
    * `run < <(python -c 'import struct;  print "A"*40 + struct.pack("<L", 0xdeadbeef)')`
* Sending some shell code with padding NOPs
    * `python -c "from struct import pack; print '\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80'.ljust(140,'\x90') +  pack('<L', 0xffffd0e0)"  > /tmp/var`

## Misc

### Disable ASLR
```bash
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
gcc test.c -o test  -fno-stack-protector -z execstack -m32
```

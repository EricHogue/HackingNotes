# Buffer Overflow

## Using a File As Input In Radare 2
```bash
echo -e "12345678901234\x67\x05\x40" > over.txt
r2 -A -d ./executable
dor stdin=over.txt
doo
```

# Upgrading Non-Interactive Shells

```bash
cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/bin/dash
/bin/bash
/bin/rbash

python --version
Python 2.7.9
python3 --version
/bin/sh: 18: python3: not found

python -c 'import pty; pty.spawn("/bin/bash")'; export TERM=xterm

perl -e 'exec "/bin/bash";'
```
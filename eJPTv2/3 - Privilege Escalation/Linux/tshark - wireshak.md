## tshark

Protocol Hierarchy

```bash
student@attackdefense:~$ tshark -r HTTP_traffic.pcap -z io,phs -q

===================================================================
Protocol Hierarchy Statistics
Filter:

eth                                      frames:30418 bytes:24643014
  ip                                     frames:30413 bytes:24642732
    udp                                  frames:1882 bytes:228368
      dns                                frames:1882 bytes:228368
    tcp                                  frames:28531 bytes:24414364
      http                               frames:1455 bytes:1705881
        data-text-lines                  frames:189 bytes:362230
          tcp.segments                   frames:102 bytes:259949
        image-jfif                       frames:165 bytes:444708
          tcp.segments                   frames:145 bytes:343160
        image-gif                        frames:75 bytes:44670
          tcp.segments                   frames:6 bytes:7911
        ocsp                             frames:73 bytes:62621
          tcp.segments                   frames:5 bytes:2451
        media                            frames:120 bytes:217932
          tcp.segments                   frames:79 bytes:158145
        png                              frames:61 bytes:113354
          tcp.segments                   frames:30 bytes:62520
        json                             frames:29 bytes:35164
          tcp.segments                   frames:5 bytes:7115
          data-text-lines                frames:3 bytes:1744
            tcp.segments                 frames:1 bytes:917
        tcp.segments                     frames:2 bytes:490
        xml                              frames:3 bytes:3533
        urlencoded-form                  frames:2 bytes:4234
      ssl                                frames:4583 bytes:8154499
        tcp.segments                     frames:1573 bytes:4463000
          ssl                            frames:1395 bytes:4069707
      tcp.segments                       frames:6 bytes:360
        http                             frames:6 bytes:360
          data-text-lines                frames:3 bytes:180
          json                           frames:3 bytes:180
            data-text-lines              frames:3 bytes:180
  arp                                    frames:5 bytes:282
===================================================================
```

```bash
student@attackdefense:~$ tshark -r HTTP_traffic.pcap -Y 'ip.src==192.168.252.128 && ip.dst==52.32.74.91'
24168 144.928157 192.168.252.128 ? 52.32.74.91  TCP 74 48544 ? 80 [SYN] Seq=0 Win=29200 Len=0 MSS=1460 SACK_PERM=1 TSval=837027 TSecr=0 WS=1024
24214 145.179880 192.168.252.128 ? 52.32.74.91  TCP 74 48546 ? 80 [SYN] Seq=0 Win=29200 Len=0 MSS=1460 SACK_PERM=1 TSval=837089 TSecr=0 WS=1024
24233 145.236767 192.168.252.128 ? 52.32.74.91  TCP 54 48544 ? 80 [ACK] Seq=1 Ack=1 Win=29200 Len=0
24241 145.475893 192.168.252.128 ? 52.32.74.91  TCP 54 48546 ? 80 [ACK] Seq=1 Ack=1 Win=29200 Len=0
24276 145.878151 192.168.252.128 ? 52.32.74.91  HTTP 493 GET /420046.gif?partner_uid=o9JecfYE-vSFC1OCbXDJnra2LQPPRlM1ETKuEF9Onaz1rdbviK35w2TZ9SGQ7pfg HTTP/1.1
24312 146.203489 192.168.252.128 ? 52.32.74.91  TCP 54 48544 ? 80 [ACK] Seq=440 Ack=500 Win=30016 Len=0
24645 147.877429 192.168.252.128 ? 52.32.74.91  HTTP 521 GET /420046.gif?partner_uid=o9JecfYE-vSFC1OCbXDJnra2LQPPRlM1ETKuEF9Onaz1rdbviK35w2TZ9SGQ7pfg&redirect=1 HTTP/1.1
24772 148.196810 192.168.252.128 ? 52.32.74.91  TCP 54 48546 ? 80 [ACK] Seq=468 Ack=1119 Win=31304 Len=0
26345 156.200222 192.168.252.128 ? 52.32.74.91  TCP 54 [TCP Keep-Alive] 48544 ? 80 [ACK] Seq=439 Ack=500 Win=30016 Len=0
26835 158.196558 192.168.252.128 ? 52.32.74.91  TCP 54 [TCP Keep-Alive] 48546 ? 80 [ACK] Seq=467 Ack=1119 Win=31304 Len=0
29102 166.228525 192.168.252.128 ? 52.32.74.91  TCP 54 [TCP Keep-Alive] 48544 ? 80 [ACK] Seq=439 Ack=500 Win=30016 Len=0
29225 168.211953 192.168.252.128 ? 52.32.74.91  TCP 54 [TCP Keep-Alive] 48546 ? 80 [ACK] Seq=467 Ack=1119 Win=31304 Len=0
29853 173.206316 192.168.252.128 ? 52.32.74.91  TCP 54 48544 ? 80 [FIN, ACK] Seq=440 Ack=500 Win=30016 Len=0
29954 173.228854 192.168.252.128 ? 52.32.74.91  TCP 54 48546 ? 80 [FIN, ACK] Seq=468 Ack=1119 Win=31304 Len=0
30364 173.610539 192.168.252.128 ? 52.32.74.91  TCP 54 48546 ? 80 [ACK] Seq=469 Ack=1120 Win=31304 Len=0
30412 174.324657 192.168.252.128 ? 52.32.74.91  TCP 54 48544 ? 80 [ACK] Seq=441 Ack=501 Win=30016 Len=0
```

```bash
tshark -r HTTP_traffic.pcap -Y 'http.request.method==GET'
tshark -r HTTP_traffic.pcap -Y 'http.request.method==GET' -Tfields -e frame.time -e ip.src -e http.request.full_uri
tshark -r HTTP_traffic.pcap -Y 'http contains password'
tshark -r HTTP_traffic.pcap -Y 'http.request.method==GET && http.host==www.nytimes.com' -Tfields -e ip.src -e ip.dst
tshark -r HTTP_traffic.pcap -Y 'ip contains amazon.in && ip.src==192.168.252.128' -Tfields -e ip.src -e http.cookie
```

## Wireshark Filters

### Find open wifi

```bash
(wlan.fc.type_subtype == 0x0008) && !(wlan.wfa.ie.wpa.version == 1) && !(wlan.tag.number == 48)
```

### Transmited or Received by MAC address
```bash
(wlan.ta == e8:de:27:16:87:18) || (wlan.ra == e8:de:27:16:87:18)
```

### Wifi Deauth

```bash
tshark -r WiFi_traffic.pcap  -Y 'wlan.fc.type_subtype == 0x000c'
```

### Show all beacons

```bash
tshark -r WiFi_traffic.pcap  -Y 'wlan.fc.type_subtype == 0x0008' -Tfields -e wlan.ssid -e wlan.bssid | sort -u
        fc:b0:c4:91:71:e1
        fc:b0:c4:91:71:e2
        fc:b0:c4:91:71:e3
Amazon Wood     c8:be:19:79:31:90
Angel Kusum     3c:1e:04:28:0b:d7
BinarySecuritySolutions bc:ae:c5:c3:5e:01
GUNEEV  54:b8:0a:58:0b:34
Home_Network    6c:19:8f:5f:81:74
Incredible Holidays     c4:12:f5:bf:de:54
LazyArtists     fc:b0:c4:91:71:e0
Logistics       6c:72:20:6b:e3:ad
Nirmall bc:f6:85:4d:b2:93
SecurityTube_Open       e8:de:27:16:87:18
Shubha  00:1e:40:ed:4b:0f
belkin.367a     94:44:52:74:e6:7a
dg_patel        ec:22:80:c3:4a:68
```
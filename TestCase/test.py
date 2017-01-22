#! /usr/bin/python
import subprocess
import time
cmdnclog = ['tcpdump', '-i','en1','tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420', 'and', 'dst', 'host' ,'103.15.200.120', '-l']

p = subprocess.Popen(cmdnclog, stdout=subprocess.PIPE)
for row in iter(p.stdout.readline, b''):
    print row.rstrip()  # process here

time.sleep(10)

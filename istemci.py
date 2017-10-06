#!/usr/bin/python3
import zerorpc
import subprocess

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:16060")

print (c.sistem())
#print (c.surum())
#print (c.mps_liste())
for item in c.ping_akis("www.google.com"): print (item)

#bir paketin kurulması
#for item in c.mps_rpc("kur","atool"): print (item)

#bir paketin bağımlılıkları
for item in c.mps_rpc("-dly","gtk2"): print (item)

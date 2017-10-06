#!/usr/bin/python3
import zerorpc
import os
import time
import subprocess

class MPS:
	
    VT ="/var/lib/pkg/DB/"
    
    def liste(self):
        dirs = os.listdir(self.VT)
        return dirs

class StreamingRPC(object):
    @zerorpc.stream
    def ping_akis(self, site):
        p = subprocess.Popen(["ping","-c","10",site], stdout=subprocess.PIPE, bufsize=1)
        return iter(p.stdout.readline, b'')
    @zerorpc.stream
    def mps_rpc(self,param,paket):
        p = subprocess.Popen(["mps",param,paket], stdout=subprocess.PIPE, bufsize=1)
        return iter(p.stdout.readline, b'')
    @zerorpc.stream   
    def streaming_range(self, fr, to, step):
        return xrange(fr, to, step)
    def sistem(self):
	    print("sistem bilgisi isteği:")
	    return ("Milis Linux Komutan Rpc Sunucu")

s = zerorpc.Server(StreamingRPC())
s.bind("tcp://127.0.0.1:16060")
s.run()

	

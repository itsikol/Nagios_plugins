#!/usr/bin/python
import os, sys, commands, itertools

exc,z_status=commands.getstatusoutput("sudo zpool list | grep -v NAME | awk '{print $9}'")
excc,d_name=commands.getstatusoutput("sudo zpool list | grep -v NAME | awk '{print $1}'")

keys = z_status.splitlines()
values = d_name.splitlines()
stname = dict(itertools.izip(keys, values))
#print stname
if all( x=='ONLINE' for x in stname.keys()) == True:
        print "All pools are fine"
        sys.exit(0)
elif 'DEGRADED' in keys and 'ONLINE' in keys:
        print stname['DEGRADED'], "this pool is DEGRADED"
        sys.exit(1)
elif all(x=='DEGRADED' for x in stname.keys()) == True:
        print "All pools are DEGRADED"
        sys.exit(2)
else:
        print"It seems you don't have any pools"
        sys.exit(3)



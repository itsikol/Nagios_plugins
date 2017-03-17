import json, sys, itertools
from collections import OrderedDict
from integralstor_common import command
dic = json.loads(open('/opt/integralstor/integralstor_unicell/config/status/master.status').read())
hostname, err = command.get_command_output('hostname', shell = True)
doc = dic[hostname[0]]
interfaces = doc['interfaces']
disks = doc['disks']
services = doc['services']
pools = doc['pools']
status_li=[]
value_li=[]

if str(sys.argv[1])=='interfaces':
  interfaces_li=[]
  for i in interfaces.iterkeys():
    for j in interfaces[i]:
      interfaces_li.append(i)
    status_li.append(interfaces[i][j])
  servicename_li= list(OrderedDict.fromkeys(interfaces_li))
  new = [str(x) for x in status_li]
  newe =[str(x) for x in servicename_li]
  nwdict = dict(zip(newe, new))
  if all(value == 'connected' for value in nwdict.values()):
    print 'All interfaces are up'
    sys.exit(0)
  elif any(value == 'disconnected' or value == 'None' for value in nwdict.values()):
    for  key, value in nwdict.items():
      if 'disconnected' == value or 'None' == value:
        value_li.append(value)
        print key, 'is down ',
    if len(value_li) > 2:
      sys.exit(2)
    else:
      sys.exit(1)
  else:
    print "something is wrong can't read status file"
    sys.exit(3)
###############################################################

elif str(sys.argv[1])=='disks':
  disks_li=[]
  for i in disks.iterkeys():
    for j in disks[i]:                      
      if j == 'status':                
        status_li.append(disks[i][j])
      elif j == 'serial_number':
        value_li.append(disks[i][j])
  nwdict = dict(zip(value_li, status_li))
  for k in nwdict:
    if nwdict[k] == 'Ok' or nwdict[k] == 'PASSED':
      print 'All disks are fine'
      sys.exit(0)
    elif nwdict[k] == None:
      print "disk:", k, "is not in good state",
      sys.exit(2)
    else:
      print 'Unable to resolve disk status'
      sys.exit(3)

####################################################################

elif str(sys.argv[1])=='services':
  services_li=[]
  for i in services.iterkeys():
    for j in services[i]:
      if type(j) == type(i):
        ppp = j.split(',')
        qqq = ppp[2].split(' ')
        status_li.append(qqq[4])
    value_li.append(i)
  nwdict = dict(zip(value_li,status_li))
  if all(v == u'active' for v in nwdict.values()):
    print 'All system services are fine'
    sys.exit(0)
  elif any(v == u'inactive' for v in nwdict.values()):
    for  key, value in nwdict.items():
      if u'inactive' == value:
        value_li.append(value)
        print key, 'is inactive ',
    if len(value_li) > 2:
      sys.exit(2)
    else:
      sys.exit(1)
  else:
    print "something is wrong can't read status file"
    sys.exit(3)

###############################################################
elif str(sys.argv[1])=='pools':
  pools_li=[]
  j= len(pools)
  for i in range(j):
    for k in pools[i].keys():
      if k == 'state' or k == 'pool_name':
        gen_li = k , pools[i][k]
        pools_li.append(gen_li)
  k= len(pools_li)
  for i in range(k):
    for j in range(2):
      if pools_li[i][j] == 'DEGRADED':
        print pools_li[i-1][j],'is DEGRADED ',
        value_li.append(pools_li[i-1][j])
  if len(value_li) == 0:
    print "All pools are fine"
    sys.exit(0)
  elif len(value_li) == 1:
    sys.exit(1)
  elif len(value_li) > 1:
    sys.exit(2)
  else:
    print "Something is wrong"
    sys.exit(3)
################################################################

else:
  print "bad argument"



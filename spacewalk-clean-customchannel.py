#!/usr/bin/python

#crude test - will rewrite better later

URL="https://vm-124.gsslab.fab.redhat.com/rpc/api"
username="admin-production"
password="redhat" # I had to reset by force the password of that user in my test satellite
import xmlrpclib
client = xmlrpclib.Server(URL)
key = client.auth.login(username,password)

channel="total_rh_server_5u8_64"

#the ids of the packages, in no specific order.
badids=[1803]
goodids=[35998]

client.channel.software.removePackages(key,channel,badids)
client.channel.software.addPackages(key,channel,goodids)
client.auth.logout(key)

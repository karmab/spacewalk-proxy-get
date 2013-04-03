spacewalk-proxy-get
===================

populate spacewalk-proxy bypassing squid for a given package or an entire channel.Search on package is case insensitive

Basic usage:

 spacewalk-proxy-get -u admin -p passwd -C your_channel -H 192.168.16.2
 
 spacewalk-proxy-get -u admin -p passwd -C your_channel -H 192.168.16.2 -P your_package
 
 wget can also be specified as download helper with -W

use -V to check packages before downloading them :

 spacewalk-proxy-get -u admin -p passwd -C a_channel -H 192.168.16.2 -V

spacewalk-proxy-get
===================

*populate spacewalk-proxy bypassing squid for a given package or an entire channel.Search on package is case insensitive*

####Basic usage:
~~~
spacewalk-proxy-get -u admin -p passwd -C your_channel -H 192.168.16.2
 
spacewalk-proxy-get -u admin -p passwd -C your_channel -H 192.168.16.2 -P your_package
~~~ 

wget can also be specified as download helper with `-W`

use -V to check packages before downloading them :

~~~
spacewalk-proxy-get -u admin -p passwd -C a_channel -H 192.168.16.2 -V
~~~

all options can be seen through the -h option

####The spacewalk-clean-customchannel script

*this script is meant to make sure that, in the mesure of the possible, only one source of signature is used for the packages in that channel.*

~~~
Usage: spacewalk-clean-customchannel [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -u USER, --user=USER  User to connect to satellite
  -p PASSWORD, --password=PASSWORD
                        Password to connect to satellite
  -c CHANNEL, --channel=CHANNEL
                        Label of the Channel to parse. Required for most
                        operations
  -H HOST, --host=HOST  Satellite hostname or ip - defaults to 127.0.0.1
  -v, --verbose         Turns up the verbosity
  -l, --list            List all the packages affected
  -a, --auto            Attempts to automatically fix the packages found
  -P PROVIDER, --provider=PROVIDER
                        Name of the provider of the package that we want to
                        find. Required for fixing the content.
  --listproviders       Make the script list the providers defined and exit.
                        only the base org admin can list the providers
~~~

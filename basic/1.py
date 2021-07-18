#!/usr/bin/env python
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link,TCLink

if '__main__' == __name__:
	net = Mininet(link=TCLink) # Get a mininet object with TCLink
    # add hosts to net object
	h1 = net.addHost('h1')  
	h2 = net.addHost('h2')
    # create link between to hosts
	Link(h1,h2)
    # build net structure
	net.build()
    # start CommandLine Interface
	CLI(net)
    # release net structure
	net.stop()

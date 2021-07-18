#!/usr/bin/env python
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link,TCLink

if '__main__' == __name__:
	net = Mininet(link=TCLink)
	h1 = net.addHost('h1')
	h2 = net.addHost('h2')
    # add hosts which using for router
	r = net.addHost('r')
    # build link
	Link(h1,r)
	Link(h2,r)
	net.build()
	CLI(net)
	net.stop()

#!/usr/bin/env python
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link,TCLink

if '__main__' == __name__:
    net = Mininet(link=TCLink) # Get a mininet object with TCLink
    # add hosts to net object
    h1 = net.addHost('h1')  
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    br1 = net.addHost('br1')
    # create link between to hosts
    net.addLink(h1,br1)
    net.addLink(h2,br1)
    net.addLink(h3,br1)
    # build net structure
    net.build()
    # clear ip addr
    h1.cmd("ifconfig h1-eth0 0")
    h2.cmd("ifconfig h2-eth0 0")
    h3.cmd("ifconfig h3-eth0 0")
    br1.cmd("ifconfig br1-eth0 0")
    br1.cmd("ifconfig br1-eth1 0")
    br1.cmd("ifconfig br1-eth2 0")
    # add bridge
    br1.cmd("brctl addbr mybr")
    # add interface to bridge
    br1.cmd("brctl addif mybr br1-eth0")
    br1.cmd("brctl addif mybr br1-eth1")
    br1.cmd("brctl addif mybr br1-eth2")
    # set bridge up
    br1.cmd("ifconfig mybr up")
    # set ip address
    h1.cmd("ifconfig h1-eth0 192.168.10.1/24")
    h2.cmd("ifconfig h2-eth0 192.168.10.2/24")
    h3.cmd("ifconfig h3-eth0 192.168.10.3/24")

    # start CommandLine Interface
    CLI(net)
    # release net structure
    net.stop()

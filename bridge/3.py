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
    h4 = net.addHost('h4')
    br1 = net.addHost('br1')
    r1 = net.addHost('r1')
    # create link between to hosts
    net.addLink(h1,br1)
    net.addLink(h2,br1)
    net.addLink(h3,br1)
    net.addLink(h4,br1)
    net.addLink(br1,r1)
    net.addLink(br1,r1)
    # build net structure
    net.build()
    # clear ip addr
    h1.cmd("ifconfig h1-eth0 0")
    h2.cmd("ifconfig h2-eth0 0")
    h3.cmd("ifconfig h3-eth0 0")
    h4.cmd("ifconfig h4-eth0 0")
    br1.cmd("ifconfig br1-eth0 0")
    br1.cmd("ifconfig br1-eth1 0")
    br1.cmd("ifconfig br1-eth2 0")
    br1.cmd("ifconfig br1-eth3 0")
    br1.cmd("ifconfig br1-eth4 0")
    br1.cmd("ifconfig br1-eth5 0")
    # add bridge
    br1.cmd("brctl addbr mybr1")
    br1.cmd("brctl addbr mybr2")
    # add interface to bridge
    br1.cmd("brctl addif mybr1 br1-eth0")
    br1.cmd("brctl addif mybr1 br1-eth1")
    br1.cmd("brctl addif mybr1 br1-eth4")
    br1.cmd("brctl addif mybr2 br1-eth2")
    br1.cmd("brctl addif mybr2 br1-eth3")
    br1.cmd("brctl addif mybr2 br1-eth5")
    # set bridge up
    br1.cmd("ifconfig mybr1 up")
    br1.cmd("ifconfig mybr2 up")
    # set ip address and route
    r1.cmd("ifconfig r1-eth0 192.168.10.254/24")
    r1.cmd("ifconfig r1-eth1 192.168.20.254/24")
    r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    h1.cmd("ifconfig h1-eth0 192.168.10.1/24")
    h1.cmd("ip route add default via 192.168.10.254")
    h2.cmd("ifconfig h2-eth0 192.168.10.2/24")
    h2.cmd("ip route add default via 192.168.10.254")
    h3.cmd("ifconfig h3-eth0 192.168.20.1/24")
    h3.cmd("ip route add default via 192.168.20.254")
    h4.cmd("ifconfig h4-eth0 192.168.20.2/24")
    h4.cmd("ip route add default via 192.168.20.254")



    # start CommandLine Interface
    CLI(net)
    # release net structure
    net.stop()

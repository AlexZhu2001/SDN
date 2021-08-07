#!/usr/bin/env python
from mininet.cli import CLI
from mininet.link import TCLink,Link,Intf
from mininet.net import Mininet
from mininet.node import Controller,RemoteController

if "__main__" == __name__:
    net=Mininet(link=TCLink)
    h1=net.addHost("h1")
    h2=net.addHost("h2")
    s1=net.addSwitch('s1')
    s2=net.addSwitch('s2')
    s3=net.addSwitch('s3')
    c0=net.addController('c0',controller=RemoteController)

    net.addLink(h1,s1)
    net.addLink(s1,s2)
    net.addLink(s1,s3)
    net.addLink(s3,s2)
    net.addLink(s2,h2)

    net.build()
    c0.start()
    s1.start([c0])
    s2.start([c0])
    s3.start([c0])

    CLI(net)
    net.stop()


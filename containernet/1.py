#!/usr/bin/python

from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller ***')
net.addController('c0')
info('*** Adding docker containers ***')
h1 = net.addHost('h1', ip='10.0.0.250/24')
d1 = net.addDocker('d1', ip='10.0.0.251/24', dimage='ubuntu:sshd1')
d2 = net.addDocker('d2', ip='10.0.0.252/24', dimage='ubuntu:sshd2')
info('*** Adding switches ***')
s1 = net.addSwitch('s1')
info('*** Creating links ***')
net.addLink(h1, s1)
net.addLink(d1, s1)
net.addLink(d2, s1)
info('*** Starting network ***')
net.start()
info('*** Runing CLI ***')
CLI(net)
info('*** Stopping network ***')
net.stop()


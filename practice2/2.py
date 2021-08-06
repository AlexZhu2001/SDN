#!/user/bin/python
from mininet.net import Containernet
from mininet.node import Docker
from mininet.cli import CLI
from mininet.log import setLogLevel,info
from mininet.link import TCLink,Link

def topology():
    net=Containernet()
    
    info("Adding hosts")
    h1=net.addHost('h1',ip='192.168.0.1/24')
    d1=net.addDocker('d1',ip='192.168.0.2/24',dimage='smallko/php-apache-dev:v10')
    h2=net.addHost('h2',ip='192.168.0.3/24')
    br1=net.addHost('br1')

    info("Create links")
    net.addLink(h1,br1)
    net.addLink(d1,br1)
    net.addLink(h2,br1)

    info("Starting network")
    net.start()
    d1.cmd("/etc/init.d/ssh start")
    br1.cmd("ifconfig br1-eth0 0")
    br1.cmd("ifconfig br1-eth1 0")
    br1.cmd("ifconfig br1-eth2 0")
    br1.cmd("brctl addbr br1")
    br1.cmd("brctl addif br1 br1-eth0")
    br1.cmd("brctl addif br1 br1-eth1")
    br1.cmd("brctl addif br1 br1-eth2")
    br1.cmd("ifconfig br1 up")

    info("Running CLI")
    CLI(net)

    info("Atopping network")
    net.stop()

if __name__=="__main__":
    setLogLevel('info')
    topology()
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

    info("Create links")
    net.addLink(h1,d1)

    info("Starting network")
    net.start()
    d1.cmd("/etc/init.d/ssh start")

    info("Running CLI")
    CLI(net)

    info("Atopping network")
    net.stop()

if __name__=="__main__":
    setLogLevel('info')
    topology()
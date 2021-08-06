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
    r1=net.addHost('r1',ip='192.168.0.254/24')
    d1=net.addDocker('d1',ip='10.0.0.1/24',dimage='smallko/php-apache-dev:v10')
    br1=net.addHost('br1')
    h2=net.addHost('h2',ip='10.0.0.3/24')
    h3=net.addHost('h3',ip='10.0.0.4/24')
    
    info("Create links")
    net.addLink(h1,r1)
    net.addLink(r1,br1)
    net.addLink(d1,br1)
    net.addLink(h2,br1)
    net.addLink(h3,br1)

    info("Starting network")
    net.start()
    d1.cmd("/etc/init.d/ssh start")
    r1.cmd("ifconfig r1-eth1 0")
    r1.cmd("ifconfig r1-eth1 10.0.0.2/24")
    r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    r1.cmd("iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -o r1-eth1 -j MASQUERADE")
    r1.cmd("iptables -A FORWARD -s 192.168.0.0/24 -p tcp --dport 80 -j REJECT")
    h1.cmd("ip route add default via 192.168.0.254")
    br1.cmd("ifconfig br1-eth0 0")
    br1.cmd("ifconfig br1-eth1 0")
    br1.cmd("ifconfig br1-eth2 0")
    br1.cmd("ifconfig br1-eth3 0")
    br1.cmd("brctl addbr br1")
    br1.cmd("brctl addif br1 br1-eth0")
    br1.cmd("brctl addif br1 br1-eth1")
    br1.cmd("brctl addif br1 br1-eth2")
    br1.cmd("brctl addif br1 br1-eth3")
    br1.cmd("ifconfig br1 up")

    info("Running CLI")
    CLI(net)

    info("Atopping network")
    net.stop()

if __name__=="__main__":
    setLogLevel('info')
    topology()
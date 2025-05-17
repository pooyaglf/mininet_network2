from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import OVSController
from mininet.log import setLogLevel
import argparse

class SingleSwitchTopo(Topo):
    def build(self, n=7):
        switch = self.addSwitch('s1')
        for h in range(n):
            host = self.addHost(f'h{h+1}')
            self.addLink(host, switch)

if __name__ == '__main__':
    setLogLevel('info')
    parser = argparse.ArgumentParser()
    parser.add_argument('--hosts', type=int, default=7)
    args = parser.parse_args()

    topo = SingleSwitchTopo(n=args.hosts)
    net = Mininet(topo=topo, link=TCLink, controller=OVSController)
    net.start()
    CLI(net)
    net.stop()


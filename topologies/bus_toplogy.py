from mininet.topo import Topo

class BusTopology(Topo):
    def build(self):
        # Create two switches (representing a bus)
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        
        # Connect the two switches together (bus connection)
        self.addLink(switch1, switch2)
        
        # Add hosts and connect them to switches
        for i in range(1, 6):
            host = self.addHost(f'h{i}')
            # First three hosts connect to switch1, the remaining to switch2
            if i <= 3:
                self.addLink(host, switch1)
            else:
                self.addLink(host, switch2)

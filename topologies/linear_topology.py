
from mininet.topo import Topo


class LinearTopology(Topo):
    def build(self):
        # Create a series of switches and hosts in a linear chain
        prev_switch = None
        for i in range(1, 6):
            switch = self.addSwitch(f's{i}')
            if prev_switch:
                self.addLink(prev_switch, switch)
            prev_switch = switch
            
            # Add host to the current switch
            host = self.addHost(f'h{i}')
            self.addLink(switch, host)

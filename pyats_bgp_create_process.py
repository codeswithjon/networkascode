from genie.testbed import load
from genie.libs.conf.interface.iosxe import Interface

testbed = load('sandboxtestbed.yaml')
device = testbed.devices['csr1000v-1']
device.connect()

def bgpconfig():
    device.configure(
            "router bgp 64500\n"
            "address-family ipv4\n"
            "neighbor 2.2.2.2 remote-as 22\n"
            "exit\n"
        )

bgpconfig()





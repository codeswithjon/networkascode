# Python
import sys
import time
import logging
import json
from genie.testbed import load
from pyats.log.utils import banner

# Enable logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)


log.info(banner("Loading testbed"))
testbed = load('sandboxtestbed.yaml')
device = testbed.devices['sbx-n9kv-ao']
device.connect()
preoutput = device.parse("show vlan")
print('====================================================')
print('VLAN DATA')
print('====================================================')
print('  ')
print('INFORMATIONAL')
print('There are' + ' ' + str(len(preoutput['vlans'])) + ' ' + 'vlans configured on this Nexus')
print('  ')
vlanList = list(preoutput['vlans'])


for vlans in vlanList:
    if vlanList != contain 14:
        device.configure(
            "vlan 14\n"
            "name @NetworkDuchys_vlan\n"
        )
    else:
        pass
preoutput = device.parse("show vlan")
print('There are' + ' ' + str(len(preoutput['vlans'])) + ' ' + 'vlans configured on this Nexus')
print('  ')
for vlans in preoutput['vlans']:
    print(vlans)

    
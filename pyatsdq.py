from genie.testbed import load
from genie.utils import Dq

tb = load('sandboxtestbed.yaml')
dev = tb.devices['csr1000v-1']
dev.connect()
new_dict = Dq(dev.parse('show interfaces')).value_operator('in_crc_errors', '>', 0).get_values('[0]')
['GigabitEthernet1']
print(new_dict)
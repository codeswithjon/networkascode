from genie.testbed import load

testbed = load('sandboxtestbed.yaml')
device = testbed.devices['csr1000v-1']
device.connect()

def licenseCheck():
    global device
    global testbed
    configregOutput = device.parse('show version')
    configregResult = configregOutput['version']['curr_config_register']
   
    if configregResult == '0x2102':
       print('Configuration register is set to reboot correctly to Start-Up Config')
    else:
       print('Please Check Configuration register')      

licenseCheck()



#!= user/bin/env Python3

# Genie/pyATS 
from genie.testbed import load

#Code to Connect to the Particular Device.
testbed = load('sandboxtestbed.yaml')
device = testbed.devices[]
device.connect()

#This is the code that does the actual command in CLI.
accessListsOutput = device.parse("show ip route")
    
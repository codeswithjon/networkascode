#!= user/bin/env Python3

# Genie/pyATS 
from genie.testbed import load

def UserInput():
    global route
    global deviceName
    route = input('What Route do you wish to find?: ')
    deviceName = input('What device do you wish to connect to?: ')

def showipRoute():
    global device
    routeTable = device.parse('show ip route' + ' ' + route)
   

UserInput()
testbed = load('sandboxtestbed.yaml')
device = testbed.devices[deviceName]
device.connect()
showipRoute()


#def deviceConnection(deviceName):
#    global load
#    global route
#    global deviceName
#    def Showiproute(route):
#        print(routeTable)
#    
#    
#       
#    Showiproute(route)
#
#deviceConnection(deviceConnection)
            
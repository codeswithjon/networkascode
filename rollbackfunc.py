def rollback():
    rollback = input('Do you wish to roll back this change? (Y/N: ')

    rollbackanswerList = ["Y", "y", "Yes", "yes", "Yeah", "yeah"]

    if rollback in rollbackanswerList:
        print('Removing VLAN' + ' ' + vlanresponse + ' ' + 'now')
        device.configure("no vlan" + ' ' + vlanresponse + "\n")
        print('VLAN' + ' ' + vlanresponse + ' ' + 'has been removed successfully\n'
            'VLAN creation program has finished'
        )
    else:
        print('VLAN' + ' ' + vlanresponse + ' ' + 'has been created successfully\n'
            'VLAN creation program has finished'
            )
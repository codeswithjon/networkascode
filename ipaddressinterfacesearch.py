from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('exampleswitch.conf', syntax='ios')

for intf_obj in parse.find_objects('^interface'):

    intf_name = intf_obj.re_match_typed('^interface\s+(\S.+?)$')

    # Search children of all interfaces for a regex match and return
    # the value matched in regex match group 1.  If there is no match,
    # return a default value: ''
    intf_ip_addr = intf_obj.re_match_iter_typed(
        r'ip\saddress\s(\d+\.\d+\.\d+\.\d+)\s', result_type=str,
        group=1, default='')
    print("{0}: {1}".format(intf_name, intf_ip_addr))
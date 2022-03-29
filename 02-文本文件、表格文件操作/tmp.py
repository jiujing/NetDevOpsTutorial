def intf_parse(text):

    interfaces = []
    lines = text.splitlines()
    for line in lines:
        if line.startswith('Eth') and not line.startswith('Ethernet'):
            infos = line.split()
            intf_name = infos[0]
            vlan = infos[1]
            type = infos[2]
            interface = {
                'intf_name': intf_name,
                'vlan': vlan,
                'type': type
            }
            interfaces.append(interface)
    return interfaces


if __name__ == '__main__':
    show_int_bri_text = '''
--------------------------------------------------------------------------------
Port   VRF          Status IP Address                              Speed    MTU
--------------------------------------------------------------------------------
mgmt0  --           up     10.10.20.95                             1000    1500    
--------------------------------------------------------------------------------
Ethernet        VLAN    Type Mode   Status  Reason                 Speed     Port
Interface                                                                    Ch #
--------------------------------------------------------------------------------
Eth1/1          1       eth  trunk  up      none                     1000(D) 11
Eth1/2          1       eth  trunk  up      none                     1000(D) 11
Eth1/3          1       eth  access up      none                     1000(D) --
Eth1/4          1       eth  access up      none                     1000(D) --
Eth1/5          --      eth  routed down    Administratively down    auto(D) --
Eth1/6          1       eth  access down    Link not connected       auto(D) --
Eth1/7          1       eth  access down    Link not connected       auto(D) --
Eth1/8          1       eth  access down    Link not connected       auto(D) --
Eth1/9          1       eth  access down    Link not connected       auto(D) --
Eth1/10         1       eth  access down    Link not connected       auto(D) --
Eth1/11         1       eth  access down    Link not connected       auto(D) --
Eth1/12         1       eth  access down    Link not connected       auto(D) --
Eth1/13         1       eth  access down    Link not connected       auto(D) --
Eth1/14         1       eth  access down    Link not connected       auto(D) --
Eth1/15         1       eth  access down    Link not connected       auto(D) --
Eth1/16         1       eth  access down    Link not connected       auto(D) --
Eth1/17         1       eth  access down    Link not connected       auto(D) --
Eth1/18         1       eth  access down    Link not connected       auto(D) --
Eth1/19         1       eth  access down    Link not connected       auto(D) --
Eth1/20         1       eth  access down    Link not connected       auto(D) --
Eth1/21         1       eth  access down    Link not connected       auto(D) --
Eth1/22         1       eth  access down    Link not connected       auto(D) --
Eth1/23         1       eth  access down    Link not connected       auto(D) --
Eth1/24         1       eth  access down    Link not connected       auto(D) --
Eth1/25         1       eth  access down    Link not connected       auto(D) --
Eth1/26         1       eth  access down    Link not connected       auto(D) --
Eth1/27         1       eth  access down    Link not connected       auto(D) --
'''
    intfs = intf_parse(text=show_int_bri_text)
    print(intfs)
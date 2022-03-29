def parse_show_int_bri(text):
    '''
    解析n9k的show int bri
    :param text: show的文本
    :return: 端口dict的list
    '''
    lines = text.splitlines()
    intfs = []
    for line in lines:
        line = line.strip()
        if line.startswith('Eth') and not line.startswith('Ethernet'):

            intf = line[0:16].strip()
            status = line[36:44].strip()
            reason = line[44:67].strip()
            intf_dict = {
                'intf':intf,
                'status':status,
                'reason':reason,
            }
            intfs.append(intf_dict)
    print(intfs)
    for i in intfs:
        print(i)

def func1():
    pass

AAA_IP = '192.168.2.167'

if __name__ == '__main__':

    text = '''
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
    parse_show_int_bri(text=text)
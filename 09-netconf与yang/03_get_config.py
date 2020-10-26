import xmltodict
from ncclient import manager
import json
from device import nexus9k_info
from device import huawei_ce_local

if __name__ == '__main__':
    ###########################################################################################
    # NETCONF filter to use for n9k
    ###########################################################################################
    netconf_filter = '''<filter>
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
            <interface></interface>
        </interfaces>
    </filter>'''
    with manager.connect(**nexus9k_info) as m:
        ## 这个config 也可以用add_interface_native  私有的yang 去配置3
        netconf_reply = m.get_config('running', netconf_filter)
        intf_details = dict(xmltodict.parse(netconf_reply.xml))
        with open('cisco_get_intfs_config.json', mode='w', encoding='utf8') as f:
            all_info = json.dump(intf_details, f, indent=4)

    ############################################################################################
    # NETCONF filter to use for huawei ce128000
    ############################################################################################
    # netconf_filter = '''<filter>
    #         <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0" >
    #             <interfaces></interfaces>
    #         </ifm>
    #     </filter>'''
    # with manager.connect(**huawei_ce_local) as m:
    #     ## 这个config 也可以用add_interface_native  私有的yang 去配置3
    #     netconf_reply = m.get_config('running', netconf_filter)
    #     intf_details = dict(xmltodict.parse(netconf_reply.xml))
    #     with open('cisco_get_intfs_config.json', mode='w', encoding='utf8') as f:
    #         all_info = json.dump(intf_details, f, indent=4)

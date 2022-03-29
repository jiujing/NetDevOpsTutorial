import xmltodict
from ncclient import manager
import pprint
from device import huawei_ce_local as dev
import json
# from device import nexus9k_info as dev

if __name__ == '__main__':
    # NETCONF filter to use
    # for n9k
    netconf_data = '''
    <cmd>
        <id>1</id>
        <cmdline>display saved-configuration time</cmdline>
      </cmd>
    '''
    with manager.connect(**dev) as m:
        # Get Configuration and State Info for Interface
        netconf_reply = m.cli(netconf_data)
        resp = xmltodict.parse(netconf_reply.xml)
        pprint.pprint(resp)

    ##################################################################################
  #   '''for huawei ce128000 '''
  #   netconf_filter_4_huawei = '''
  #   <filter type="subtree">
  #   <ethernet xmlns="http://www.huawei.com/netconf/vrp" format-version="1.0" content-version="1.0"></ethernet>
  #   </filter>
  #   '''
  #   netconf_filter_4_huawei = '''
  #       <filter type="subtree">
  #    <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
  #   </ifm>
  # </filter>
  #
  #       '''
  #   with manager.connect(**dev) as m:
  #       # Get Configuration and State Info for Interface
  #       netconf_reply = m.get(netconf_filter_4_huawei)
  #       # netconf_reply = m.get()
  #       all_info = xmltodict.parse(netconf_reply.xml)
  #       pprint.pprint(all_info)
  #       # with open('huawei_get.json', mode='w', encoding='utf8') as f:
  #       #     all_info = json.dump(all_info, f, indent=4)
  #       with open('huawei_get_intfs.json', mode='w', encoding='utf8') as f:
  #           all_info = json.dump(all_info, f, indent=4)

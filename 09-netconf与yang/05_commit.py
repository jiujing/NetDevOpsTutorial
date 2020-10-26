import xmltodict
from ncclient import manager

from device import nexus9k_info
from device import huawei_ce_local

if __name__ == '__main__':


    with manager.connect(**huawei_ce_local) as m:
        netconf_reply = m.commit()

        intf_details = dict(xmltodict.parse(netconf_reply.xml))
        print(intf_details)

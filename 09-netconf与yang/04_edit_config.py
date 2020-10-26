import xmltodict
from ncclient import manager

from device import nexus9k_info
from device import huawei_ce_local

if __name__ == '__main__':
      ####################################################################
      # n9k config
      ####################################################################
      add_interface_native = '''
    <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <intf-items>
          <svi-items>
             <If-list nc:operation="merge">
                 <id>vlan220</id>
             </If-list>
          </svi-items>
        </intf-items>
      </System>
     </config>'''

      with manager.connect(**nexus9k_info) as m:
          # Get Configuration and State Info for Interface
          ## 这个config 也可以用add_interface_native  私有的yang 去配置
          netconf_reply = m.edit_config(config=add_interface_native ,target='running')

          intf_details = dict(xmltodict.parse(netconf_reply.xml))
          print(intf_details)
          m.copy_config('running','startup')
    #####################################################################
    # n9k config
    #####################################################################
#     interface_desc_config = '''<config>
#       <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
#         <interfaces>
#           <interface>
#             <ifName>GE1/0/0</ifName>
#             <ifDescr>configed by netconf2020</ifDescr>
#           </interface>
#         </interfaces>
#       </ifm>
#     </config>
# '''
#
#     with manager.connect(**huawei_ce_local) as m:
#         netconf_reply = m.edit_config(config=interface_desc_config, target='running')
#         intf_details = dict(xmltodict.parse(netconf_reply.xml))
#         print(intf_details)
#         # m.commit()

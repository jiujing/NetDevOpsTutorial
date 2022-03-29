from nornir.core.task import Result, Task
from nornir import InitNornir
from nornir.plugins.functions.text import print_result
import nornir.plugins.connections.netconf

nt_get ='''
    <nf:filter type="subtree" xmlns:nf="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="http://www.cisco.com/nxos:7.0.3.I7.8.:if_manager" >
      <show>
        <interface/>
      </show>
    </nf:filter>'''

'''<filter>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface><name>eth1/1</name></interface>
    </interfaces>
</filter>'''
'''
<nf:rpc xmlns:nf="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="http://www.cisco.com/nxos:9.3.5.:if_manager" message-id="1">
  <nf:get>
    <nf:filter type="subtree">
      <show>
        <interface/>
      </show>
    </nf:filter>
  </nf:get>
</nf:rpc>
]]>]]>

<filter>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface><name>eth1/1</name></interface>
    </interfaces>
</filter>
'''
nr = InitNornir(
    inventory={
        "options": {
            "hosts": {
                "rtr00": {
                    "hostname": "192.168.248.140",
                    "username": "admin",
                    "password": "admin1234!",
                    "port": 830,
                    "platform": "nxos",
                    "connection_options": {
                        "netconf": {"extras": {"hostkey_verify": False,"timeout":180}}
                    },
                }
            }
        }
    }
)

def netconf_code(task: Task) -> Result:
    manager = task.host.get_connection("netconf", task.nornir.config)

    # get running config and system state
    print(manager.get(nt_get))

    # get candidate config


    return Result(result="ok", host=task.host)


result = nr.run(task=netconf_code)
print_result(result)

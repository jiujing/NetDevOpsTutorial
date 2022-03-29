import ruamel.yaml

logger = logging.getLogger(__name__)

NOS_IP_NAME = 'ip'


def _get_connection_options(data: Dict[str, Any]) -> Dict[str, ConnectionOptions]:
    cp = {}
    for cn, c in data.items():
        cp[cn] = ConnectionOptions(
            hostname=c.get("hostname"),
            port=c.get("port"),
            username=c.get("username"),
            password=c.get("password"),
            platform=c.get("platform"),
            extras=c.get("extras"),
        )
    return cp


def _get_defaults(data: Dict[str, Any]) -> Defaults:
    return Defaults(
        hostname=data.get("hostname"),
        port=data.get("port"),
        username=data.get("username"),
        password=data.get("password"),
        platform=data.get("platform"),
        data=data.get("data"),
        connection_options=_get_connection_options(data.get("connection_options", {})),
    )


def _get_inventory_element(
        typ: Type[HostOrGroup], data: Dict[str, Any], name: str, defaults: Defaults
) -> HostOrGroup:
    if 'ssh_timeout' in data.get('data', {}):
        data['connection_options'] = {
            'netmiko':
                {
                    'extras': {
                        'conn_timeout': int(data['data']['ssh_timeout'])
                    }
                }
        }
    return typ(
        name=name,
        hostname=data.get("hostname") or data.get("ip"),
        port=data.get("port"),
        username=data.get("username"),
        password=data.get("password"),
        platform=data.get("platform"),
        data=data.get("data"),
        groups=data.get(
            "groups"
        ),  # this is a hack, we will convert it later to the correct type
        defaults=defaults,
        connection_options=_get_connection_options(data.get("connection_options", {})),
    )


class CMDBInventory:
    def __init__(
            self,
            devices: List[dict],
    ) -> None:
        """
        根据devices的字典列表加载所有网络主机

        Args:

          host_file: path to file with hosts definition
        """
        # devices = [
        #     {'hostname': 'sbx-nxos-mgmt.cisco.com', 'username': 'admin', 'password': 'Admin_1234!', 'port': 8181,
        #      'platform': 'cisco_nxos'}
        # ]
        host_info = ['hostname', 'username', 'password', 'port', 'platform', 'ip', 'secret', 'device_type']
        group_info = ['hostname', 'username', 'password', 'port', 'platform']
        reshape_devices = []
        for device in devices:
            reshape_device = {
                'data': {}
            }
            for k, v in device.items():
                if k in host_info:
                    if k == 'device_type':
                        reshape_device['platform'] = v
                    else:
                        reshape_device[k] = v
                else:
                    reshape_device['data'][k] = v
            reshape_devices.append(reshape_device)

        self.deivces = reshape_devices

    def load(self) -> Inventory:
        '''
        username: admin
      password: Admin
      port: 22
      platform: XXX
        :return:
        '''
        hosts = Hosts()
        groups = Groups()
        defaults = Defaults()
        hosts_dict = {i['ip']: i for i in self.deivces}
        for name, host_dict in hosts_dict.items():
            hosts[name] = _get_inventory_element(Host, host_dict, name, defaults)
        return Inventory(hosts=hosts, groups=groups, defaults=defaults)
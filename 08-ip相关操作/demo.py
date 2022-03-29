from netaddr import IPNetwork, IPAddress


def subnet(ip_net, ip_list, new_prefix):
    ip_net_obj = IPNetwork(ip_net)
    subnets = ip_net_obj.subnet(int(new_prefix))
    subnets = list(subnets)
    resp_data = []
    for subnet_obj in subnets:
        pure = is_pure_subnet(subnet_obj, ip_list)
        info = {
            'ip_net': subnet_obj,
            'pure': pure,
            'used': not pure,
        }
        resp_data.append(info)
    return resp_data


def is_pure_subnet(subnet, ip_list):
    for ip in ip_list:
        if IPAddress(ip) in subnet:
            return False
    return True


if __name__ == '__main__':
    data = subnet('192.168.10.0/24', ['192.168.10.2','192.168.10.67'], 26)
    print(data)

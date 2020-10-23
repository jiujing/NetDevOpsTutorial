import ipaddress
from netaddr import IPNetwork,IPGlob,IPRange,cidr_merge,IPAddress,IPSet
if __name__ == '__main__':
    ipset1 = IPSet(['192.0.2.0']) | IPSet(['192.0.2.1']) | IPSet(['192.0.2.2']) | IPSet(['192.0.2.3']) | IPSet(
        ['192.0.2.4'])
    ipset2 = IPSet(['192.0.2.4'])
    print('ipset1-ipset2', ipset1 - ipset2)
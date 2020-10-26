from ncclient import manager
from device import huawei_ce_local as dev
# from device import nexus9k_info as dev

# import logging
#
# logging.basicConfig(
#     level=logging.INFO,
# )

if __name__ == '__main__':

    with manager.connect(**dev) as m:
        '''
        # 根据设备的netconf软件层面实现的情况，部分不支持。
        # 传入module的name，唯一标识
        '''
        module_name  = 'openconfig-interfaces'
        schema = m.get_schema(module_name)
        with open("{}.yang".format(module_name), 'w') as f:
            # Write schema
            f.write(schema.data)
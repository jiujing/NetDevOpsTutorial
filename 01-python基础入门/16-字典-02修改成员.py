if __name__ == '__main__':
    """
    key值存在，再次赋值会更新原有的值
    key值不存在，赋值，会创建新的k，v对
    """
    dev_info = {
        'dev_name': 'sw01',
        'ip': '192.168.1.1',
        'ssh_port': 22
    }
    print('dev_info修改前', dev_info)
    dev_info['dev_name'] = 'sw02'
    print('dev_info修改后', dev_info)

    #
    dev_info['username'] = 'admin'
    print('dev_info更新后', dev_info)

    # 删除kv值，del方法，不安全
    del dev_info['ssh_port']
    print('dev_info删除ssh_port后', dev_info)

    # 会报错
    # del dev_info['ssh_port']
    # print('dev_info删除ssh_port后', dev_info)

    # pop 删除，同时把删除的v返回,可以指定默认值，可以避免k值不存在报错
    deleted_v1 = dev_info.pop('ssh_port', None)
    deleted_v2 = dev_info.pop('dev_name', None)
    print('dev_info删除ssh_port后', dev_info)
    print('deleted_v1', deleted_v1)
    print('deleted_v2', deleted_v2)

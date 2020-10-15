from netmiko import SSHDetect, Netmiko,ConnectHandler
# Netmiko等同于ConnectHanler

if __name__ == '__main__':
    device = {
        'device_type': 'autodetect',  # 设备类型使用autodetect ，netmiko会去设备上自动执行命令，判断是什么类型的设备
        'host': '192.168.199.102',
        'username': 'admin',
        'password': 'admin123!',
        'port': 22,
    }
    # 创建一个Detect的对象，将参数赋值
    guesser = SSHDetect(**device)

    # 调用autodetect ，进行device_type的自动判断，返回结果是一个最佳结果的字符串，这个字符串就是netmiko自动判断的device_type
    # 无法判断的时候返回的是None
    best_match = guesser.autodetect()
    #
    print('best_match is:{}'.format(best_match))
    # 有一个潜在可能的device_type的字典，但是目前意义不大，了解即可。
    print('all guessers  is:{}'.format(guesser.potential_matches))

    device['device_type'] = best_match
    connection = Netmiko(**device)
    # 然后就可以去执行相关的命令了

    # 获取回显的前缀，提示符，prompt。可以从中获取设备名称，可以梳理资产信息。
    print('prompt is :{}'.format(connection.find_prompt()))

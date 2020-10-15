from netmiko import ConnectHandler

if __name__ == '__main__':
    '''
    send_config_set 一次推多行，我们想去逐行推送，并根据回显做一些处理，比如报错了就终止推送
    这个时候我们要关注2个参数
    enter_config_mode=False 在执行前显视的调用enable()
    exit_config_mode=True  推送完 不离开config 模式 推送下一行
    
    '''
    net_conn = ConnectHandler(device_type='cisco_ios',
                              host='192.168.199.102',
                              username='admin',
                              password='admin123!',
                              port=22,  # 可选参数, 默认是22端口，可以不写，在模拟环境可能会有端口映射，或者是使用Telnet等可以指定其他端口
                              secret='admin123!'  # 选填，, 默认值是''，空字符串,这个是enable的密码
                              )
    net_conn.enable()
    print('check_enable_mode!!!!!!!!!!!',net_conn.check_enable_mode())
    output = net_conn.config_mode()
    is_config = net_conn.check_config_mode()
    print('is_config!!!!!!!!!!!!!!',is_config)
    print('output!!!!!!!!!!!!!!',output)
    config_lines = [
        'interface Ethernet0',
        'description configed by netmiko20201015',
    ]
    success = True
    for line in config_lines:
        output = net_conn.send_config_set(config_commands=[line],
                                      exit_config_mode=False,enter_config_mode=False)
        print(output)
        if '^' in output:
            print('fail')
            success = False
            break
    if success:
        net_conn.exit_config_mode()
        output = net_conn.save_config()
        print(output)
    else:

        print('配置失败')
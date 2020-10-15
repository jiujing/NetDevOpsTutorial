'''
net_connect.send_command()  # 向下发送命令，返回输出（基于模式）
net_connect.send_command_timing()  # 沿通道发送命令，返回输出（基于时序）
net_connect.send_config_set()  # 将配置命令发送到远程设备
net_connect.send_config_from_file()  # 发送从文件加载的配置命令
net_connect.save_config()  # 将running#config保存到startup#config
net_connect.enable()  # 输入启用模式
net_connect.find_prompt()  # 返回当前路由器提示符
net_connect.commit()  # 在Juniper和IOS#XR上执行提交操作
net_connect.disconnect()  # 关闭连接
'''

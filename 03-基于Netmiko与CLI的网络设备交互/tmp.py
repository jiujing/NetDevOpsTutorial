from netmiko import ConnectHandler
from dev_info import nxosv9k

if __name__ == '__main__':
    '''
    通过ConnectHandler ，输入设备类型 ip(host) 用户名密码 端口（默认是ssh的22）等
    这其实是一个函数，它会根据你的device_type给你用对应的类实例化成对象
    '''

    dev_info = {
        'device_type': 'cisco_ios',
        'host': '192.168.199.102',  # 用host 和ip均可，系统会自动判断
        'username': 'admin',
        'password': 'admin123!',
        'port': 22,  # 默认是22端口，可以不写，在模拟环境可能会有端口映射，或者是使用Telnet等可以指定其他端口
        'secret': 'admin123！',  # 选填，, 默认值是''，空字符串,这个是enable的密码
    }

    # 简单脚本建议使用with ，上下文管理 在退出的时候自动关闭连接，graceful
    with ConnectHandler(**dev_info) as net_conn:
        output = net_conn.send_command('show version')
        print(output)

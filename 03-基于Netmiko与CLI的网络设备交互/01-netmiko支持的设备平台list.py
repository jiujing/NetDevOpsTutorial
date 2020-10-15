from netmiko.ssh_dispatcher import platforms

if __name__ == '__main__':
    '''
    netmiko 是基于paramiko封装的一个支持多厂商的ssh工具包
    实现对设备的ssh（telnet）登陆操作，部分支持文件传输
    Multi-vendor library to simplify Paramiko SSH connections to network devices
    github地址：https://github.com/ktbyers/netmiko
    安装：pip install netmiko
    依赖：
        Paramiko >= 2.4.3
        scp >= 0.13.2
        pyserial
        textfsm
    根据适配程度各平台的支持分为以下三种
                Regularly Tested
                Limited Testing
                Experimental
    对于设备采集，个人认为适配程度非常好，封装程度非常高，非常适合网络运维开发新手。
    '''
    for platform in platforms:
        print(platform)

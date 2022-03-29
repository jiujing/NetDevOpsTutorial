from netmiko import ConnectHandler,Netmiko
from dev_info import nxosv9k
def ssh_dev_show():
    with Netmiko(**nxosv9k) as conn:
        log = conn.send_command(command_string='show int bri')
        return log


def write_log(text):
    with open('zy.log',mode='a',encoding='utf8') as f:
        f.write(text)

if __name__ == '__main__':
    log = ssh_dev_show()
    print(log)
    write_log(text=log)


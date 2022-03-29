import paramiko
import time
def push_config_2_device(ip,username, password, configs, port=22,err_signs=['^'],success_signs=[]):
    success_flag = True
    ssh_session = paramiko.SSHClient()
    ssh_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_session.connect(ip,port=port,username=username,password=password,allow_agent=False,look_for_keys=False)

    device_connect = ssh_session.invoke_shell()

    outputs = []
    for config in configs:
        device_connect.send(config.encode('utf8'))
        time.sleep(5)
        output = device_connect.recv(650000)
        outputs.append(output.decode('utf8'))

    for output in outputs:
        for err_sign in err_signs:
            if err_sign in output:
                success_flag = False
                break
    return {
        'success':success_flag,
        'outputs':outputs
    }


if __name__ == '__main__':
    '''
    hostname: sbx-nxos-mgmt.cisco.com
  username: admin
  password: Admin_1234!
  port: 8181

    '''
    ip = 'sbx-nxos-mgmt.cisco.com'
    username = 'admin'
    password = 'Admin_1234!'
    port = 8181
    configs = ['show version']
    outputs = push_config_2_device(ip=ip,username=username,password=password,port=port,configs=configs)
    print(outputs)
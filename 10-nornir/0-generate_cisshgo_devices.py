import yaml


def generate_deivce_objs(start=10011, end=10040, ip='127.0.0.1', username='admin', password='admin',
                         platform='cisco_ios', extra={'show_version_cmd': 'show version'}):
    dev_objs = {}
    for index, i in enumerate(range(int(start), int(end))):
        dev_obj = {
            'hostname': ip,
            'username': username,
            'password': password,
            'port': i,
            'platform': platform,
            'data': extra
        }
        dev_objs[f'dev{index}'] = dev_obj
    return dev_objs


def pass_python_obj_into_yaml(yaml_data, filepath):
    with open(filepath, 'w') as f:
        y = yaml.dump(yaml_data, f)


if __name__ == '__main__':
    data = generate_deivce_objs()
    pass_python_obj_into_yaml(data, './inventory/cisshgo.yaml')

from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_get

nr = InitNornir(
    # config_file="nornir.yaml"
)

dev_info_by_napalm_get = nr.run(
    napalm_get, getters=['interfaces', 'facts', 'interfaces_ip', 'environment'])

print_result(dev_info_by_napalm_get)

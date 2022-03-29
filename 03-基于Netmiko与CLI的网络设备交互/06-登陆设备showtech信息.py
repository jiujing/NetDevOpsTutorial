import logging
import time

from netmiko import Netmiko

logging.basicConfig(
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    dev_info = {
        'device_type': 'cisco_nxos',
        'host': 'sbx-nxos-mgmt.cisco.com',
        'username': 'admin',
        'password': 'Admin_1234!',
        # 'secret': 'secret',  # optional, defaults to ''
        # 'session_log': 'show_demo.log',  # 保存到指定文件，完整的呈现整个登录和执行命令的过程
        'timeout': 60,
        'conn_timeout': 30
    }
    cmd = 'show running'

    output_last2search = ''
    # 执行相关命令的超时时间 默认5分钟
    timeout = 60*5
    # 每次读取channel中内容的停顿延时
    read_delay = 0.5
    # 计算出超时所需要的循环次数
    max_loops = timeout / read_delay
    # 是否执行成功，默认失败，只有读到指定回显则代表成功，置位
    success = False
    # 初始化循环计数器
    loop = 1

    with Netmiko(**dev_info) as net_conn:
        with open(f"{cmd.replace(' ', '_')}.log", encoding='utf8', mode='w') as f:
            logger.info('计算当前的回显')
            prompt = net_conn.find_prompt()
            # 根据当前回显计算一个大概范围值，以便在后续channel读取回的字符串确定是否读取到指定prompt，相关命令回显结束停止循环
            search_prompt_range = len(prompt)+2
            logger.info(f'current promt:{prompt}')

            output = ''
            logger.info('开始执行命令')
            # 向ssh的channel中发送命令
            # 先清空现有的channel中的数据
            net_conn.read_channel()
            net_conn.write_channel(f'{cmd}\n')
            while loop < max_loops:
                logger.debug(f'loop is {loop}')
                # 读取channel中的返回
                data = net_conn.read_channel()
                # 停顿一下，方便下次循环读取数据
                time.sleep(read_delay)
                loop += 1
                # 统一换行符为'\n'
                data = data.replace('\r\n', '\n')
                logger.debug(f"read channel:{data}")
                # 如果有回显字符串则写入，同时查找是否有命令结束的回显，以便跳出循环
                if data:
                    f.write(data)
                    if len(data) > search_prompt_range:
                        output_last2search = data
                    else:
                        output_last2search += data
                    output_last2search = output_last2search[0 - search_prompt_range:]
                    logger.debug(f"search prompt in :{data}")
                    logger.debug(f"output_last2search:{output_last2search}")
                    if prompt in output_last2search:
                        success = True
                        break
        if success:
            logger.info('发现回显，收集结束')
        else:
            logger.info('未发现回显，任务超时结束，请适当调整超时时间')

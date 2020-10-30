 ansible-doc -l    # 列出 Ansible 支持的模块

 ansible-doc ping  # 查看该模块帮助信息
 
 ansible-hoc快速执行模块
 hosts文件可以执行，默认加载/etc/ansible/hosts 
 group_name可以指定执行哪一组，
 module_name是调用的模块名称，默认是command,网络设备用raw或者cli_command 
 -a 是模块用的参数
 查看模块可以 ansible-doc module_name查看
 
 ansible -i <hosts文件>  group_name -m module_name -a "args"
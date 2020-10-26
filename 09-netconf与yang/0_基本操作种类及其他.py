import pprint

from ncclient import manager

if __name__ == '__main__':
    '''ncclient支持的操作类型'''
    pprint.pprint(manager.OPERATIONS, indent=4)
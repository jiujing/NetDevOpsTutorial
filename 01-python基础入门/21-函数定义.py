'''
函数定义：
def func_name(arg1,arg2,arg3=3,arg4=4):

    code_block

    return value
return根据实际情况，可有可无，return的vlaue可有可无，无的时候等同于不写return等同于rerun None
def fun():
    ...
x= fun()
print(x)
'''

def fun():
    ...


def say_something(name, something='你好'):
    print('{}说:“{}”'.format(name, something))

    return None


if __name__ == '__main__':
    # say_something('xiaoming', 'Hello!')
    # say_something('xiaoming')
    say_something(name='xiaoming',something='我叫小明')

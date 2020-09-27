class Switch(object):
    def __init__(self,interfaces):
        self.interfaces = interfaces

    def show_interfaces(self):
        for i in self.interfaces:
            print(i)


def yanshi_duixaing():
    intfs = ['1/1', '1/2', '1/3']
    s = Switch(interfaces=intfs)
    # s.show_interfaces()
    print(s.interfaces)
    s.show_interfaces()
if __name__ == '__main__':
    ...


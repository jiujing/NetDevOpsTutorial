class Switch(object):
    def __init__(self,interfaces):
        self.interfaces = interfaces

    def show_interfaces(self):
        for i in self.interfaces:
            print(i)



if __name__ == '__main__':

     intfs = ['1/1','1/2','1/3']
     s = Switch(interfaces=intfs)
     # s.show_interfaces()
     print(s.interfaces)
     s.show_interfaces()

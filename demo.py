"""class name:
    def __init__(self) -> None:
        self.name='bini'
        self.age=19
        self.scul='aau'
        self.com=self.computer()
    def show(self):
        print(self.name, self.age,self.scul)
        return self.s1.show()
        
    class computer:
        def __init__(self) -> None:
            self.type='acer'
            self.cpu="i5, 4 logical processors "
            self.memory="8GB"
        def show(self):
            print("He has",self.type,", core",self.cpu,self.memory)
    s1=computer()
s1=name()
s1.show()
class a:
    def __init__(self):
        print("am bini")
    def detail():
        print("i have a son")
class b:
    def __init__(self):
        super().__init__()
        print("life is good")
    def detail():
        print("am his son")
class c(a,b):
    def inheritance(self):
        super().detail()# we use this super method when we 
abebe=c()
c.detail()

abebe.__init__()
#polymorphism
#duck typing
class vscode:
    def execute(self):
        print("here are too many extensions ")
class pycharm:
    def execute(self):
        print("here are a lot of features")
class properties:
    def code(self,ide):
        ide.execute()
ide=pycharm()
lap1=properties()
properties().code(ide)
#operator oveloading
print('{} {}'.format('bini','dagi'))
class overloading:
    def __init__(self,m1,m2) -> None:
        self.m1=m1
        self.m2=m2
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
o1=overloading(1,2)
o2=overloading(2,3)
print(o2)
class this_store:
    def __init__(self) -> None:
        self.mtools=[]
        self.ctools=['glass','aluminium']
    def maintainance(self):
            m=input('enter the reqeuest:')
            self.mtools.append(m)
            if "robenito" in self.mtools:
                print('utilize new')
    def warehouse(self):
        need=input('enter the request:')
        def site_x(need):
             return need
        if site_x(need)=="glass":
            print('{}'.format('give him glass'))
tool1=this_store()
tool2=this_store()
tool1.warehouse()
tool2.maintainance()
from abc import ABC,abstractmethod 
class computer:
    @abstractmethod
    def process(self):
        print('there we go')
com=computer()
com.process()
from threading import *
from time import sleep
class com(Thread):
    def run(self):
        for i in range(50):
            print('playing')
            sleep(1)
class moc(Thread):
    def run(self):
        for i in range(50):
            print('learning')
            sleep(1)
c1=com()
c2=moc()
values=c1.start()
values=c2.start()
c1.join()
c2.join()
print("bye")"""



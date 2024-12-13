from Developer import Developer
from BackEndDeveloper import BackEndDeveloper   
from FrontEndDeveloper import FrontEndDeveloper
from PythonDeveloper import PythonDeveloper

dev1 = PythonDeveloper("John", "Doe", 5, 1000)
dev2 = FrontEndDeveloper("Jane", "Doe", 3)
dev3 = BackEndDeveloper("Jim", "Doe", 4)
dev4 = Developer("Jack", "Doe", 35)

for x in (dev1, dev2, dev3, dev4):
    x.develop()
    x.code()
    print(x)
    print()

print(dev4.age)

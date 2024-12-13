from BackEndDeveloper import BackEndDeveloper

class PythonDeveloper(BackEndDeveloper):
    def __init__(self, firstName, lastName, experience ,salary):
        super().__init__(firstName, lastName ,experience)
        self.salary = salary

    def code (self):
        print(f"{self.firstName} is coding in Python")

    


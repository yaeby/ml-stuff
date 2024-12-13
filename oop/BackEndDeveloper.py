from Developer import Developer

class BackEndDeveloper(Developer):
    def __init__(self, firstName, lastName, experience):
        super().__init__(firstName, lastName)
        self.experience = experience

    def develop(self):
        super().develop()
        print(f"{self.firstName} {self.lastName} is developing the app's back")
    
    def code(self):
        super().code()
from Developer import Developer

class FrontEndDeveloper(Developer):
    def __init__(self, firstName, lastName, experience):
        super().__init__(firstName, lastName)
        self.experience = experience

    def develop(self):
        super().develop()
        print(f"{self.firstName} {self.lastName} is developing the app's front")

    def code(self):
        super().code()
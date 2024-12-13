class Developer:
    def __init__(self, firstName, lastName, age=None):
        self.firstName = firstName
        self.lastName = lastName
        self.__age = age

    def develop(self):
        print(f"{self.firstName} {self.lastName} is developing something, click click ...")

    def code(self):
        print(f"{self.firstName} is coding, type type ...")

    def __str__(self):
        return f"Developer: {self.firstName} {self.lastName} {self.__age}"

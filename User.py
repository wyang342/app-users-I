# your User class goes here
class User:
    def __init__(self, name="Default", email_address="example@example.com", license_number=123123123):
        self.name = name
        self.email_address = email_address
        self.license_number = license_number

    def interact(self):
        return "interacted!"

    def __str__(self):
        return "I am {}, my email is {}, and my license number is {}.".format(self.name, self.email_address, self.license_number)


rob = User("Rob", "rob@gmail.com", 123321123)
john = User("John", "john@outlook.com", 333333333)
mack = User("Mack", "mack@mail.com", 444444333)
print(rob)
print(john)
print(mack)

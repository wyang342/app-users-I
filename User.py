# your User class goes here
class User:
    name = "Bob"
    email_address = "bob@google.com"
    license_number = 123123123

    def __init__(self, name, email_address, license_number):
        self.name = name
        self.email_address = email_address
        self.license_number = license_number

    def interact(self):
        return "interacted!"

    def __str__(self):
        return "I am {}, my email is {}, and my license number is {}.".format(self.name, self.email_address, self.license_number)


rob = User("Rob", "rob@gmail.com", 123321123)
print(rob)

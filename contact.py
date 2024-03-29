
#Contact class

class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

# Accessor Method: only returns a value
    def get_name(self):
        return self.__name

# Mutation method: only modifies a value
    def set_name(self, name):
        self.__name = name

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return f"Name: {self.__name}\nPhone: {self.__phone}\nEmail: {self.__email}"

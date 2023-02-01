
class EmailUnittestClass:
    def __init__(self):
        self.email=''
        inputm =input(f"Introducir Email: {self.email}")
        self.email = inputm
        

    def email_requerimientos(self):
       print(self.email)
       print(self.email.find("@"))
       assert self.email.find("@") != -1

    def email_punto(self):
        print(self.email)
        print(self.email.find(".com"))
        assert self.email.find(".com") != -1


Unittest = EmailUnittestClass()
Unittest.email_requerimientos()
Unittest.email_punto()














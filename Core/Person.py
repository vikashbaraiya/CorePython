class Person():
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname


    def getFullname(self):
        return self.firstname,self.lastname


    def __str__(self):
        return self.firstname

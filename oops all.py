"""we make all oops concept here to use"""

class College:
    college_name="UPTU"

    '''making constructor '''
    def __init__(self,name,password=None):
        self.name=name
        self.__password=password

    '''access class varriable using class method either acess with class name'''
    @classmethod
    def getCollegeName(cls):
        return cls.college_name

    '''all method inside class are instance varriable and using private varriable for data abstraction'''
    def setPassword(self,name,password):
        if self.name==name:
            self.__password=password
            return True
        return "Write correct user name"

    def getPassword(self):
        if self.__password is None:
             return "First set password"
        return self.__password


class Department(College):
    departmentname="Electronics"

    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject





obj=Department("Gaurav","Maths")
print(obj.getPassword())
print(obj.setPassword("Gaurav",123))
print(obj.name)
print(obj.getPassword())



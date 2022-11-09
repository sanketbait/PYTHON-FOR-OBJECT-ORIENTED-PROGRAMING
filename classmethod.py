
class Person:
    count_instance = 0
    def __init__(self, f_name, l_name, age):
        Person.count_instance += 1
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
    
    @classmethod
    def count_instances(cls):
        # return f"you have created {cls.count_instance} instances of  {cls. __name__} class"
    
    # def full_name(self):
    #     return f"{ self.first_name} {self.last_name}"
    
    # def is_above_18(self):
    #     return(self.age >18


p1 = Person('harshit', 'vashistha', 10)
p2 = Person('anish', 'waghw',16)
# p3 = Person('akshay','rtyu', 25)
# p4 = Person('rudransh', 'qwerty', 15)
print(Person.count_instances())


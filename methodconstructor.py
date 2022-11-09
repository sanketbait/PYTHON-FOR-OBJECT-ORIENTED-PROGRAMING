# class method as a constructor
class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instabce of {cls.__name__}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age > 18

p1 = Person("sanket","bait",21)
p2 = Person("sourabh","kamble",25)
print(p1.full_name())
print(p2.is_above_18())
print(Person.full_name(p2))
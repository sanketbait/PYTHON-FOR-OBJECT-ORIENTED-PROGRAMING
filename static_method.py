# oop -static method in python
# class method as a constructor
class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @classmethod
    def from_string(cls, string):
        first,last, age =string.split(',')
        return cls(first,last,age)
    
    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instabce of {cls.__name__}"
    
    @staticmethod
    def hello():
        print("hello, static method called")
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age > 18

p1 = Person("sanket","bait",21)
p2 = Person("sourabh","kamble",25)
# p3 = Person.from_string('krutik,navale,23')
# print(p3)
# print(Person.from_string(p2))
Person.hello()


# INSTANCE METHOD
class Person :
    def __init__(self,f_name,l_name,age):
        # instance variable
        self.first_name = f_name
        self.last_name = l_name
        self.p_age= age
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.p_age>18

p1 = Person('sanket', 'bait',21)
p2 = Person('tushar','suvre',12)
# print(p1.first_name)
# print(p1.last_name)
# print(p2.last_name)
print(Person.full_name(p1))
print(p2.full_name())
print(p1.is_above_18())
print(Person.is_above_18(p2))


l =[1,2,3,4,5]
# print(l)
# l.clear()
list.clear(l)
# l.append(10)
print(l)

# list.append(l,10)
# print(l)
# l.append(10)
# print(l)


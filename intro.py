# list class
# list object
# list method

class Person :
    def __init__(self,f_name,l_name,age):
        # instance variable
        self.first_name = f_name
        self.last_name = l_name
        self.p_age= age

p1 = Person('sanket', 'bait',21)
p2 = Person('tushar','suvre',22)
print(p1.first_name)
print(p1.last_name)
print(p2.last_name)
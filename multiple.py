#  MULTIPLE INHERITANCE
class A:
    def class_a_method(self):
        return f"it is just a 'A' class method"
    
    def hello(self):
        return "hello class A"

class B:
    def class_b_method(self):
        return f"it is just a 'B' class method"
    
    def hello(self):
        return "hello class B"

class C(A,B):
    pass

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(issubclass(C,B))
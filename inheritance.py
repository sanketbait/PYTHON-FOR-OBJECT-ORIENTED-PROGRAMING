#  inhritance 
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def make_a_call(self,phone_number):
        print(f"calling on : {phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super(). __init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

phone1 = Phone('oppo','oppo123', 25000)
phone2 = Smartphone('apple','a1',75000,'32gb','128gb','30px')
print(phone1.full_name())
print(phone2.internal_memory)
print(phone2. __dict__)
print(phone1._price)
print(Phone.full_name(phone2))
print(issubclass(Smartphone,Phone))
print(isinstance(phone2,Smartphone))

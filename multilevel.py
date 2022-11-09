# MULTILEVEL INHERITANCE

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

    def full_name(self):
        return f"{self.brand} {self.model_name} and rear camera is  {self.rear_camera}"  # this is called method overloading

class Megaphone(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,battery_power,front_camera):
        super(). __init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.battery_power = battery_power
        self.front_camera = front_camera

    def feature(self):
        return f"{self.battery_power} and front camera is {self.front_camera}"



phone1 = Phone('oppo','oppo123', 25000)
phone2 = Smartphone('apple','a1',75000,'32gb','128gb','30px')
phone3 = Megaphone('apple','a1',75000,'32gb','128gb','30px','200h','40px')
print(phone2.full_name())
print(Phone.full_name(phone1))
print(Smartphone.full_name(phone2))
print(phone3.feature())
print(phone3. __dict__)
print(issubclass(Smartphone,Phone))
print(issubclass(Megaphone,Smartphone))
print(issubclass(Smartphone,Phone))
print(isinstance(phone3,Smartphone))
print(isinstance(phone1,Smartphone))
print(isinstance(phone3,Phone))
print(isinstance(phone2,Megaphone))
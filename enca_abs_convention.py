#  

class Phone:
    def __init__(self, brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
    
    def make_a_call(self,phone_number):
        print(f"calling on : {phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass

phone1 = Phone('oppo','oppo123',25000)
print(Phone.full_name(phone1))
print(Phone.make_a_call(phone1,1234567890))
print(phone1. __dict__)
print(Phone.send_message(phone1))
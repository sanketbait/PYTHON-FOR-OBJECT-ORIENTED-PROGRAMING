class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price
        # self._price = max(price,0)
        # if price > 0:
        #     self._price =
        # else:
        #     self._price =
         

        # self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}"
    
    #getter() ,setter()
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

    def make_a_call(self,phone_number):
        print(f"calling on : {phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone2 = Phone("nokia",'nokiapro',20000)
print(phone2.brand)
print(Phone.full_name(phone2))
print(phone2._price)
print(phone2.complete_specification)
print(phone2.make_a_call(1234567890))
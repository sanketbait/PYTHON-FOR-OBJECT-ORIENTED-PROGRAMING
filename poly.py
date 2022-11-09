
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def phone_name(self):
        return f"{self.brand} {self.model_name}"

    #str, repr
    def __str__(self):
        return f"phone({self.brand} {self.model_name} and price is {self._price})"

    def __repr__(self):
        # return f"{self.brand} {self.model_name} and price is {self._price}"
        return f'Phone(\'{self.brand}\',\'{self.model_name}\',{self._price})'
    
    def __add__(self,other):
        return self._price + other._price
        # return self._price * other._price

my_phone  = Phone("NOKIA","NOKIAPRO",20000)
# print(str(my_phone))
# print(repr(my_phone))
# print(my_phone.__repr__())
# print(my_phone.__str__())
# print(len(my_phone))
# print(my_phone._price)
# print(my_phone.__add__(2000))
print(Phone.__add__(my_phone,2000))
# class Mobile:
#     discount_percent = 10
#     def __init__ (self, name,model,price):
#         self.mobile_name = name
#         self.model_name = model
#         self.mobile_price = price
#     def apply_discount(self):
#         # off sale = (num/100) * self.mobile_price
#         off_sale = (Mobile.discount_percent/100) * self.mobile_price
#         return self.mobile_price - off_sale

# mob1 = Mobile('APPLE','APPLE123',75000)
# mob2 = Mobile('ONEPLUS','ONEPLUS123',35000)
# mob3 = Mobile('REALME','NARZO20',20000)
# mob4 = Mobile('LG','LG123',15000)
# mob5 = Mobile('OPP0','OPPOPRO',25000)

# print(mob1.apply_discount())
# print(Mobile.apply_discount(mob1))

# # print(mob1.mobile_name)
# # print(mob1.apply_discount(10))
# # print(mob2.apply_discount(10))
# # print(mob3.apply_discount(10))
# # print(mob4.apply_discount(10))
# # print(mob5.apply_discount(10))


'''******part2******'''
class Mobile:
    discount_percent = 10
    def __init__ (self, name,model,price):
        self.mobile_name = name
        self.model_name = model
        self.mobile_price = price
    def apply_discount(self):
        # off sale = (num/100) * self.mobile_price
        off_sale = (self.discount_percent/100) * self.mobile_price
        return self.mobile_price - off_sale
Mobile.discount_percent = 30   # discount
mob1 = Mobile('APPLE','APPLE123',75000)
mob2 = Mobile('ONEPLUS','ONEPLUS123',35000)
mob3 = Mobile('REALME','NARZO20',20000)
mob4 = Mobile('LG','LG123',15000)
mob5 = Mobile('OPP0','OPPOPRO',25000)

print(mob1. __dict__)
print(mob1.apply_discount())
print(Mobile.apply_discount(mob1))
mob2.discount_percent = 50
print(mob2. __dict__)
print(mob2.apply_discount())

# print(mob1.mobile_name)
# print(mob1.apply_discount(10))
# print(mob2.apply_discount(10))
# print(mob3.apply_discount(10))
# print(mob4.apply_discount(10))
# print(mob5.apply_discount(10))
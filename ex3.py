class Laptop:
    count_instance = 0
    def __init__(self, brand , name ,price):
        # print("these are various laptops")
        # instance variable
        Laptop.count_instance += 1
        self.brand_name = brand
        self.laptop_name = name
        self.price = price

laptop1 = Laptop('hp','hp23455',50000)
laptop2 = Laptop('lenovo','lenevovl4',35000)
laptop3 = Laptop('acer','qwel4',25000)
laptop4 = Laptop('dell','sdfgl4',45000)
laptop6 = Laptop('mac','asdfg5645',80000)
print(Laptop.count_instance)
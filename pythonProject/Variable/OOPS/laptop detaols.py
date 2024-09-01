class laptop:
    def __init__(self, lap_brand, lap_processor, hd, ram, price):
        self.brand = lap_brand
        self.processor = lap_processor
        self.hd = hd
        self.ram = ram
        self.price = price

s1 = laptop("dell", "Intel", "1TB", "16GB", 1000)
print(s1.brand)
print(s1.processor)
print(s1.price)


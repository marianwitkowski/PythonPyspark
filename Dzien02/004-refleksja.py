
# Refleksja
class Product:
    def __init__(self, p1, p2, p3, p4, p5):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5

    def __str__(self):
        return f"{self.p1}, {self.p2}, {self.p3}, {self.p4}, {self.p5}"

product = Product(1,2,3,4,5)
props = [item for item in dir(product) if item.startswith("p") ]
print(props)
for prop in props:
    curr_value = getattr(product, prop)
    print(f"{prop} - {curr_value}")
    setattr(product, prop, curr_value*10)

delattr(product, "p2") # usuwanie property dla obiektu
setattr(product, "p10", "ABC")
setattr(product, "p2", "ABC")
print(product)
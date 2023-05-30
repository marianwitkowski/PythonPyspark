
# Programowanie zorientowane obiektowo

class MetaProduct:
    pass

class Product:

    def __init__(self, id, name, price):
        self.__product_id = id # a'la prywatne
        self.name = name # publiczne
        self._price = price  # a'la chronione

    def get_info(self):
        return f"ID={self.__product_id}, Nazwa={self.name}, Cena={self._price}"

    def set_price(self, new_price):
        self._price = new_price

    def __str__(self):
        return f"(__str__) ID={self.__product_id}, Nazwa={self.name}, Cena={self._price}"

# deklaracja obiektu klasy Product
coca_cola = Product(1, "Coca-Cola 1L", 8.12)
coca_cola._price = 9.99
coca_cola.name = "XYZ"
coca_cola.__product_id = 2
coca_cola._Product__product_id = 2
print(coca_cola.get_info())
print(coca_cola)

coca_cola.set_price(7.99)
print(coca_cola.get_info())
coca_cola.price = 8.99
print(coca_cola.get_info())

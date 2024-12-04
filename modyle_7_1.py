from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

class Shop(Product):

    def __init__(self, name, weight, category, __file_name = 'products.txt'):
        self.__file_name = __file_name

    def get_products(self, __file_name):
        str = __file_name
        file = open(self.__file_name 'r')
        pprint(file.read())
        file.close()

    def add(self, *products):
       if i in products:
            print(f'Продукт уже есть в магазине')
        __file_name.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())







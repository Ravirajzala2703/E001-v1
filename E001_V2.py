class Category:
    code = 0

    def __init__(self, cat_name, perent=None) -> None:
        self.cat_name = cat_name
        self.perent = perent
        self.code = Category.code+1
        self.no_of_product = 0
        Category.code += 1
        self.products = []
        self.display_name = self.cat_name
        self.displayy_name()

    def __repr__(self) -> str:
        return 'category:{}'.format(self.cat_name)
    def dis(self):
        print('category: ', self.cat_name , 'code: ',self.code)
        print(self.display_name)
        print('no_of_product->>>: ',self.no_of_product)
        if self.no_of_product != 0:
            print('Name of product')
            for i in self.products:
                print(i.name)
        print()

    def displayy_name(self):
        count = self

        while (count.perent != None):
            self.display_name = f'{count.perent.cat_name} > {self.display_name}'
            count = count.perent

class Product:
    product_code = 0

    def __init__(self,name,category,price,stock_at_location={}) -> None:
        self.name = name
        self.code = Product.product_code+1
        Product.product_code += 1
        self.category = category
        self.price = price
        category.no_of_product += 1
        category.products.append(self)
        self.stock_at_location=stock_at_location

    def display(self):
        print("Product :", self.name, "code: ", self.code, "category: ", self.category.cat_name, "Price: ", self.price)



# parent objects
vehicale = Category("vehicale")
food = Category("Food")
electronics = Category("electronics")
footware  = Category("footware")
# child objects
cars = Category("cars", vehicale) 
wefer= Category("wefer", food)
television = Category("television", electronics)
# child of child
petrol = Category("petrol", cars)
balaji = Category("balaji", wefer)
sony = Category("sony", television)

cat_list = [vehicale, food, electronics,footware, cars, wefer, television, petrol, balaji, sony]

productlist = [Product("masala chips", wefer, 20),
        Product("ciaz", cars, 1700000),
        Product("i20", cars, 700000),
        Product("sony bravia", television, 15000),
        Product("sony A19", television, 18000),
        Product("temeto chips", wefer, 10),
        Product("xuv 700", cars, 2100000),
        Product("sony 32inch", television, 20000),
        Product("cream onion chips", wefer, 40),
        Product("brezza", cars, 1250000),
        Product("puma shoes",footware, 1500),
        Product("nike sandal",footware, 400),
        Product("peragon chappal",footware, 200),
        Product("scooter",vehicale, 55000),
        Product("mazza",food, 55000),
        Product("home theater",electronics, 120000)]

print('list of category')
cat_list.sort(key=lambda x:x.cat_name.lower())
print(cat_list)
for x in cat_list:
    x.dis()
print('----------------------------------------------------------------')
print('list of product')
for x in productlist:
    x.display()
print('-----------------------------------------------------------------')
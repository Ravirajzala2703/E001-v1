class Category:
    def __init__(self,cat_name,cat_code):
        self.cat_name = cat_name
        self.cat_code = cat_code
        self.no_of_product = 0
    def show(self):    
        print('============================================================================================')
        print('Name of category: ',self.cat_name)
        print('Code of category:',self.cat_code) 
        print('No_of_product is: ',self.no_of_product)
        print('============================================================================================')

class Product(Category):
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code 
        self.category = category
        category.no_of_product = category.no_of_product + 1
        self.price = price
    def __repr__(self):
            return '(product_name: {}, product_code: {}, product_cat: {},product_price:{}\n)'.format(self.name, self.code, self.category.cat_name, self.price)

cat1 = Category('car','cr154b14')
cat2 = Category('bike','bk125n136')
cat3 = Category('scooter','sc135k35')

p1 = Product('swift','sw1545f45',cat1,750000)
p2 = Product('i20','ir215fv4',cat1,640000)
p3 = Product('verna','vc25j56',cat1,1015301)
p4 = Product('passion x','px546df4',cat2,70000)
p5 = Product('cd100','cd51d4ef',cat2,75580)
p6 = Product('i smart','si41fd54d',cat2,65411)
p7 = Product('splender','sl154f4',cat2,60000)
p8 = Product('activa','ac35fd1f',cat3,88100)
p9 = Product('jupiter','jp31f54v',cat3,78999)
p10 = Product('access','ss55fd4',cat3,90400)
cat1.show()
cat2.show()
cat3.show()

mylist = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
for i in range(0,len(mylist)-1):
    for j in range(len(mylist)-1):
        if(mylist[j].price > mylist[j+1].price):
            mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
print('***********************:PRODUCT PRICE LOW TO HIGH:************************\n',mylist)
for i in range(len(mylist)-1):
    for j in range(len(mylist)-1,i,-1):
        if(mylist[j].price > mylist[i].price):
            mylist[i].price,mylist[j].price = mylist[j].price, mylist[i].price
print('***********************:PRODUCT PRICE HIGH TO LOW:************************\n',mylist)

pro_code = input('Enter product code: ')
for i in mylist:
    if pro_code == i.code:
        print(i)







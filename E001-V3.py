import E001_V2
from E001_V2 import Product,Category

class Location:
    location_code = 1000
    def __init__(self,name):
        self.name=name
        self.code=Location.location_code+1
        Location.location_code+=1
    def dis_play(self):
        print("location name:", self.name, "code", self.code)


class Movement:

    def __init__(self,from_location,to_location,product,quantity):
        self.from_location=from_location
        self.to_location=to_location
        self.product=product
        self.quantity=quantity
        # self.display=''
        
        try:
            print('\nproduct_name:',product.name,'\nFrom_location: >>',self.from_location.name,'To_location: >>',self.to_location.name,'quantity: >>',self.quantity)
            if self.from_location in self.product.stock_at_location:
                
                if self.product.stock_at_location[self.from_location] >= self.quantity:  # 40 >=20
                    qun = self.product.stock_at_location[self.from_location] - self.quantity  # 40-20=20
                    self.product.stock_at_location.update({self.from_location: qun})  # {jamnagar,20}
                    if self.to_location in self.product.stock_at_location:  # {bhavnagar}it check location is available or not
                        qun1 = self.product.stock_at_location[self.to_location] + self.quantity  # 10+20
                        self.product.stock_at_location.update({self.to_location: qun1})  # {bhavnagar,30}
                else:
                #     # if not available location it add both location and quantity
                    self.product.stock_at_location.update({self.to_location: self.quantity})
                print(self.product.name,"done movement")
                # self.display = f'product quantity :{self.quantity} from {self.from_location.name} to {self.to_location.name}'

            else:
                print(f"quantity no: {self.quantity} of {self.product.name} not available {self.from_location.name}")
        except Exception:
            print("no location for that product\n")

    @staticmethod
    def movements_by_product(product):
        move = []
        for item in listofm:
            if item.product.name == product.name:
                move.append(item)
    
        return move

rajkot = Location("Rajkot")
jamnagar = Location("Jamnagar")
bhavnagar = Location("Bhavnagar")
mumbai = Location("Mumbai")
location_list = [rajkot, jamnagar, bhavnagar, mumbai]
for i in location_list:
    i.dis_play()

vehicale = Category("vehicale")

car = Product('car',vehicale,1450000,{rajkot:30, jamnagar:40, mumbai:25})
scooter = Product('scooter',vehicale,75000,{rajkot:30,jamnagar:10,bhavnagar:10})
bike = Product('bike',vehicale,88500,{jamnagar:40,bhavnagar:40,mumbai:10})
e_bike = Product('E_bike',vehicale,120000,{rajkot:30,bhavnagar:90,mumbai:10})
bicycle = Product('bicycle',vehicale,7000,{rajkot:2,jamnagar:95,bhavnagar:10,mumbai:100})

listofprodcut = [car, scooter, bike, e_bike, bicycle]

for i in listofprodcut:
    print(i.name)  # print name of product
    for key in i.stock_at_location:  # print dictionary of location name,quantity value
        print(f'{key.name} - {i.stock_at_location[key]}')
    print()

movement1 = Movement(jamnagar, bhavnagar, bicycle, 50)
movement2 = Movement(rajkot, bhavnagar, car, 20)
movement3 = Movement(rajkot, jamnagar, scooter, 20)
movement4 = Movement(jamnagar,bhavnagar, bike, 10)
movement5=Movement(jamnagar,rajkot,e_bike,30)

listofm = [movement1, movement2, movement3, movement4,movement5]
print()

for product in listofprodcut:
    product_move_list = Movement.movements_by_product(product)

print("\n")
print("---------------------------------------------------------------------")
print("new stock at location")
for i in listofprodcut:
    i.display()
    print('Location: ',end='')
    for key in i.stock_at_location:
        print(f'{key.name} - {i.stock_at_location[key]}', end='  ')
    print('\n')
print("product list by location")
for i in location_list:
    print(i.name)
    for p in listofprodcut:
        if i in p.stock_at_location:
            print(f'{p.name} - {p.stock_at_location[i]}')
    print()
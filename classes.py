#this part for storing the details of the customer
import pickle
import datetime

class Customer:

  def __init__(self, name, address, phone):
    self.name = name
    self.address = address
    self.phone = phone

  def __str__(self):
    return f"Name :{self.name} \nAddress : {self.address} \nPhone : {self.phone}"

  def update(self, state):
    print(f"Dear {self.name} , Your order has been reached {state} status ")


class Mechanic:

  def __init__(self, name, phone, address):
    self.name = name
    self.address = address
    self.phone = phone
    self.ordersassigned = []
    self.sort_order = []

  def get_orders(self):
    date = []
    for i in self.ordersassigned:
      if i.entrydate.date() == datetime.datetime.today().date():
        date.append(i.deliverydate.date())
    date.sort()
     
    
    for j in date:
      for i in self.ordersassigned:
        if i.deliverydate.date() ==  j:
          self.sort_order.append(i)
     
    for k in self.sort_order:
      print(k)
      
      
  def update_status (self):
    for i in set(self.sort_order) :
      i.job_card.change_status()
      print(i.job_card)

  


# state design pattern for updating status
class Status:

  def change_status(self):
    pass


class Order_Placed(Status):

  def change_status(self):
    return Mechanic_Assigned()


class Mechanic_Assigned(Status):

  def change_status(self):
    return Inprocess()


class Inprocess(Status):

  def change_status(self):
    return Completed()


class Completed(Status):

  def change_status(self):
    print("Completed")


class Jobcard:

  def __init__(self, order):
    self.order = order
    self.status = Order_Placed()

  def get_status(self):
    return type(self.status).__name__

  def change_status(self):
    self.status = self.status.change_status()
    if self.get_status() == "Completed":
      self.order.customer.update("Completed")
      
  def __str__(self):
    return f"**********************************************************JOB CARD ****************************************** \nCUSTOMER NAME : {self.order.customer.name} \nADDRESS : {self.order.customer.address} \nPHONE : {self.order.customer.phone} \nVEHICLE TYPE : {self.order.vehicle_type} \nENGINE NO : {self.order.engine_no} \nNO.OF.SERVICES : {len(self.order.services)} \nMECHANIC ADDRESS : {self.order.order_assigned.name} \nDELIVERY DATE {self.order.deliverydate.date()} \nCOST : {self.order.cost} \nSTATUS : {self.get_status()} \n**********************************************************WELCOME AGAIN **************************************"
 

# decorator design pattern for services with various functionality
class Service:

  def cost(self):
    return 50

  def __str__(self):
    return "Service"


class ServiceDecorator(Service):

  def __init__(self):
    super().__init__()
    self.status = None

  def cost(self):
    return super().cost()


class PunctureDecorator(ServiceDecorator):

  def cost(self):
    return super().cost() + 200


class WaterwashDecorator(ServiceDecorator):

  def cost(self):
    return super().cost() + 100


class BrakecheckDecorator(ServiceDecorator):

  def cost(self):
    return super().cost() + 50


class OilserviceDecorator(ServiceDecorator):

  def cost(self):
    return super().cost() + 50

class Order:
  orders = {}
  count = 0
  mechanics = []


  def __init__(self, customer, vehicle_type, engine_no):
    self.customer = customer
    self.vehicle_type = vehicle_type
    self.engine_no = engine_no
    self.services = []
    self.entrydate = datetime.datetime.today()

  def delivery_date(self):
    x = len(self.services) * 24
    self.deliverydate = self.entrydate + datetime.timedelta(hours=x)
    return self.deliverydate.date()

  def service(self, type):

    if type == "puncture":

      service = PunctureDecorator()
      self.services.append(service)
      self.cost = service.cost()

    elif type == "waterwash":
      service = WaterwashDecorator()
      self.services.append(service)
      self.cost = service.cost()

    elif type == "brakecheck":
      service = BrakecheckDecorator()
      self.services.append(service)
      self.cost = service.cost()

    elif type == "oilservice":
      service = OilserviceDecorator()
      self.services.append(service)
      self.cost = service.cost()

  def add_service(self, type):
    self.service(type)

  
  def order_assign(self):

    if Order.count >= 3:
      Order.count = 0
    self.order_assigned = Order.mechanics[Order.count]
    self.order_assigned.ordersassigned.append(self)
    Order.count +=1
    
    

  def __str__(self):
    return f"\nCustomer : {self.customer.name} \nVehicle type : {self.vehicle_type} \nEngine no : {self.engine_no} \nNo .of.Services : {len(self.services)} \ndelivery date :{self.delivery_date()}  "

  def finish(self):
  
    self.delivery_date()
    self.job_card = Jobcard(self)
    self.customer.update("Order placed !")
    self.order_assign()
    print(self.job_card)
    with open('orders.pickle', 'ab') as handle:
      pickle.dump(self, handle, protocol=pickle.HIGHEST_PROTOCOL)

  def total_orders(self):
    return Order.count

# this part is for placing the order with required details


# mech1 = Mechanic("Brad", 4377877, "Door 10")
# mech2 = Mechanic("Chloe", 578192678, "Lane 40")
# mech3 = Mechanic("Dan", 456789, "Door 50")
# Order.mechanics.append(mech1)
# Order.mechanics.append(mech2)
# Order.mechanics.append(mech3)

# customer = Customer("monisha", "road street", 345768)
# order = Order(customer, "bike", 264)
# order.service("puncture")
# order.add_service("waterwash")
# order.finish()


# customer1 = Customer("man", "riss street", 434778)
# order1 = Order(customer1, "motor", 897)
# order1.service("puncture")
# order1.add_service("waterwash")
# order1.finish()




# customer2 = Customer("janani", "wide street", 89765457)
# order2 = Order(customer2, "cycle", 1064)
# order2.service("oilservice")
# order2.add_service("brakecheck")
# order2.finish()




# customer3 = Customer("monkey", "narrow street", 9786533366)
# order3 = Order(customer3, "scooter", 1276)
# order3.service("brakecheck")
# order3.finish()

# print(1)
# mech1.get_orders()
# print(2)
# mech2.get_orders()
# print(3)
# mech1.get_orders()

# mech1.update_status()
# mech1.update_status()
# mech1.update_status()






# return the total orders by giving the date as input;
def today_orders(date):
  with open('orders.pickle', 'rb') as handle:
    
    while 1:
      try:
        b = pickle.load(handle)
        if b.entrydate == date :
          print(b)
        
        
      except EOFError:
        break
      
# todays_orders = today_orders(datetime.datetime.today().date())

def total_orders():
  with open('orders.pickle', 'rb') as handle:
    count = 0
    while 1:
      try:
        pickle.load(handle)
        count += 1
      except EOFError:
        break
  print(count)
  
# total = total_orders()
# print(total)
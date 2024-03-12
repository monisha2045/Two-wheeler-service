from login import *
from classes import *


class Template():
    def register(self,name,pasword) :
        pass
    
    def create_customer(self,name,address,phone):
        pass
    
    def create_order(self,customer,vehicle_type,engine_no) :
        pass
    
    def add_service(self,order,name):
        pass
    
    def finish(self,order):
        pass
    
    def get_order(self,mechanic):
        pass
    
    def update(self,mechanic):
        pass
    
    def process(self):
        name = input("Enter a user name :")
        password = input("Enter a password :")
        a = self.register(name,password)
        
        if a:
            name = input("Enter a customer name :")
            address = input("Enter a address of the customer :")
            phone = int(input("Enter a phone number :"))
            cust = self.create_customer(name,address,phone)
            
            vehicle = input("Enter a vehicle type :")
            engine = input("Enter an engine number :")
            order = self.create_order(cust,vehicle,engine)
            
            print(" 1 ----> add services \n TYPE The SERVICE AS BELOW \n puncture \n waterwash \n brakecheck \n oilservice \n 2 ----> finish")
            num = int(input("Enter a number : "))
            while num != 2:
                service = input("Enter a service from the options above :")
                self.add_service(order,service)
                num = int(input("Enter a number to continue or exit : "))
                
            self.finish(order)
        else:
            print("Please Sign")
            self.process()
        
class Two_wheel_service(Template):
    
    def register(self, name, password):
        Register(name,password)
        return Register.login(name,password)
        
    def create_customer (self,name,address,phone):
        return Customer(name,address,phone)
        
    def create_order(self, customer, vehicle_type, engine_no):
        return Order(customer,vehicle_type,engine_no)
        
    def add_service(self, order ,name):
        order.add_service(name)
        
    def finish(self,order):
        order.finish()
        
    def get_order(self,mechanic):
        mechanic.get_orders()
    
    def update(self,mechanic):
        mechanic.update_status()

# two_wheel_service = Two_wheel_service() 

# #creating the mechanics
# mech1 = Mechanic("Brad", 4377877, "Door 10")
# mech2 = Mechanic("Chloe", 578192678, "Lane 40")
# mech3 = Mechanic("Dan", 456789, "Door 50")

# #adding the mechanics to the order class
# Order.mechanics.append(mech1)
# Order.mechanics.append(mech2)
# Order.mechanics.append(mech3)
 
# two_wheel_service.process() 
# two_wheel_service.process()
# two_wheel_service.process()
# two_wheel_service.process()
# mech1.get_orders()

# mech1.update_status()
# mech1.update_status()
# mech1.update_status()
# class Vehicle:
#     name = None
#     Model = None
#     def get_detail(self,name,model):
#         self.name= name
#         self.model = model
#     def detail(self):
#         print(f"{self.name}-{self.model}")
# p1 = Vehicle("honda","CR-V")
# p1.detail()


# pillers of object oriented programming ()

class Car:
    brand = None
    model = None
    
    def __init__(self,brand, model):
        self.brand= brand
        self.model= model
    
    def detail (self):
        print(f"brand:{self.brand}-Model:{self.model}")

c1 = Car("bmw","bmw-10") 
# objects c1 --> Car
c1.detail ()



# class Ev(Car):
#     pass
# ev1 = Ev(Car)
# ev1.get_detail("ev","234")
# ev1.detail(Car)
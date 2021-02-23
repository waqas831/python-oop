class Vehicle:

  def first(self,car_name,max_speed,milage,price):
    self.car_name=car_name
    self.max_speed=max_speed
    self.milage=milage
    self.price=price

  def show(self):
    return "car name is", self.car_name, "their max_speed is",self.max_speed, "and their milage is", self.milage,"and price is",self.price

obj=Vehicle()
obj.first('mahran',234,324,22344)
print(obj.show())
class Welcome:
  def __init__(self,name,year,semester,roll):
    self.name=name
    self.year=year
    self.semester=semester
    self.roll=roll

class Detail(Welcome):
  pass

obj1=Detail("waqas",2020,4,9)
obj2=Detail("usman",2020,4,19)
print(obj1.name,obj1.year,obj1.semester,obj1.roll)
print(obj2.name,obj2.year,obj2.semester,obj2.roll)
print(obj1.name,obj1.year,obj1.semester,obj1.roll)
print(obj2.name,obj2.year,obj2.semester,obj2.roll)

'''print("hello world"); 
a=int(input("enter first number"));
b=int(input("enter second  nuber"));
c=a+b;
print(c);'''
import  random
#class and objects
class HelloWorld:
  def message(self):
    print("welcome in python programming")

  def sum(self,a,b):
    c=a+b
    print(c)

  def random_no(self):
    print(random.randint(1,234))

  def calculator(self,first,second):
    self.first=first
    self.second=second
    print("1)add    2)sub      3)multiply     4)divide")
    choice=int(input("enter your choice"))
    if(choice==1):
      print(first+second)
    elif(choice==2):
      print(first-second)
    elif(choice==3):
      print(first*second)
    elif(choice==4):
      print(first/second)
    else:
      print("invalid choice")    
      

a=HelloWorld()
a.message()
a.sum(23,34)
a.random_no()
a.calculator(23,34)
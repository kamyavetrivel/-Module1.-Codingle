class cat:
    def __init__(self,name,age):
        self.name=name 
        self.age=age 
    def info(self):
       print(f"Im a cat, my name is {self.name} and i am {self.age} years old  ")
    def make_sound(self):
       print("sound note is meow") 

class dog:
   def __init__(self,name,age):
      self.name=name
      self.age=age
   def info(self):
      print(f"im a dog, my name is{self.name} and i am {self.age} yearls old")
   def make_sound(self):
       print("sound note is bark") 

cat1= cat("gina",93)
dog1= dog("rio",83.0)
for animal in (cat1,dog1):
   animal.make_sound()
   animal.info()


      
    
   
    

class Person( object ):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber= idnumber 
    def diplay(self):
        print(self.name)
        print(self.idnumber)

class employee(Person):
   def __init__( self, name, idnumber, salary, post):
       self.salary= salary
       self.post=post

       Person.__init__(self,name,idnumber) 
   
   a= employee('python',8797234760,92000030000, 'intern')
   a.display()

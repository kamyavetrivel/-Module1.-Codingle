class employee:
    def __init__ (self):
        print("employee created")
    def __del__ (self):
        print("empoyee deleted")
obj= employee() 
del obj 

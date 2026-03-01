class Expression:

    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add(self):
        result = self.num1 + self.num2 + self.num3
        print("The result is:", result)


# Creating object
obj1 = Expression(10, 20, 30)

# Calling method
obj1.add()

def recur_factorial(n):
    if n==1:
        return n 
    else: 
        return n*recur_factorial(n-1) 
num=int(input("enter number")) 
if num<0:
    print("sorry factorial doesnt exist")
elif num ==0:
    print("factorial for 0 is 1")
else:
    print("the factorial of number is",recur_factorial(num))
     

Height=float(input("enter your height"))
Weight= float(input("enter your weight"))
bmi=Weight/(Height/100)**2
print("bmi of the user is",bmi)
if bmi<=18.4: 
    print("your are underweight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=29.9:
    print("you are slightly overweight")
elif bmi<=39.9:
    print("you are obese")
else:
    print("you are extremely obese")
    
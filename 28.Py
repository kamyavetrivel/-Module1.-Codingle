print("Hello, im ai chatbot, what is your name?")
name=input()
print(f"hello{name}")
print("how are you feeling today?(good/bad)")
feeling= input().lower() 

if feeling == "good": 
    print("glad your doing well")
elif feeling== "bad": 
    print(" sorry to hear that, hope your doing better")
else:
    print("i know it is hard to put on your feelings")
print(f"it was nice talking to you {name} goodbye") 
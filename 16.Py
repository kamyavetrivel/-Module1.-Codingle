list= ["red","yellow","blue","green","purple"] 

print("length of list:",len(list))
print("first Element:",list[0])
print("last Element",list[-1])

list.append("grey")
print("appended List::",list)

list.remove("purple")
print("removed list:",list)

list.sort()
print("sorted list:",list)

list.pop(1)
print("List after popping:",list )

list.reverse()
print("list is reversed:",list) 

list=list [0:3]
print("slice list is",list)

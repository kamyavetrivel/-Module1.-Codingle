class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("blu",38)
wo=parrot("wo",92) 
print("blu is the{}".format(blu.species))
print("wo is the{}".format(wo.species))
print("{} is {} year old ".format(blu.name,blu.age))
print("{} is {} year old ".format(wo.name,wo.age))

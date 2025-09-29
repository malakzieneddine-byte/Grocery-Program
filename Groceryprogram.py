groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}
cart=[]

item = ""

while (item!= "done"):
    item = input("What do you want to buy(type done when you finish): ")
    if (item in groceries):
        cart.append(item)
    else:
       if (item!="done"):
        print("Sorry,  we don’t have that item")    

print("You bought: ",cart)
cost=0

for item in cart:
      cost+=groceries[item]

print("Your cost= ",cost)



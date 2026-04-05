#  shoppiing cart
food= []
prices =[]
total=0

while True :
    food_item = str(input("Please enter the food Item to buy:  (enter q to Quit) "))
    if food_item.lower() == 'q' :
        break
    else:
        food.append(food_item)

    price= input("Please enter the price for the item in Rupees: (enter q to Quit) ")
    if price.lower() == 'q'  : 
        break
    else:
        price=float(price)
        prices.append(price)
    

for f in food: 
    print(f)

for p in prices: 
    total=total+p 
print(f"Total bill of the order is {total} rupees")  
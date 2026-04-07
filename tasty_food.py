menu= {'pop_corn' : 15 ,'french fries' : 60 ,'dosa' : 40}
Cart_bill=0
cart=[]
order_flag =input("Would you like to order something ? (Y/N)")
if order_flag.upper() =='Y':
    print("-----MENU-----")
    for F ,V in menu.items():
        print(f"{F:20}:{V}") 
    orders=[]

    while True:
        
        orders=input("Enter your item to add to cart (q-Quit & Got to cart) ")

        if orders.lower()=='q':
            break
        elif menu.get(orders) is not None :
            cart.append(orders)
    

    if cart is not None:
        print(cart)
        for c in cart:
            Cart_bill =Cart_bill + menu.get(c)

        print(f"Your total bill is {Cart_bill : 2} Rupees")
else:
    print("Will miss you ")



        







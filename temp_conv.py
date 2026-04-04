unit  =input("please input your unit of temperature C/F : ")
temp= float(input("enter temperature : "))

if unit.upper() == 'C':
    temp= round((temp*9/5)+32,1)
    print(f"{temp} F")

elif unit.upper() =='F' : 
    temp= round((temp -32 )*5/9,1)
    print(f"{temp} C")

    pass

else:
    print(f"{unit} is an invalid unit of measurement")
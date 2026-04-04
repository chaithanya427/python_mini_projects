weight = float(input("enter the weight : "))
unit = input("Enter the unit Kilograms or Pounds (KG or L) : ")

if unit.upper() == 'KG' :
    weight =round(weight * 2.204,3)
    print(f"Your weight is : {weight}{unit}")
elif unit.upper() == 'L' :
    weight =round((weight / 2.204),3)
    print(f"Your weight is : {weight}{unit}")

else:
    print(f"{unit} is not valid")


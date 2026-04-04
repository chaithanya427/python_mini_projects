# a(final amount)=p (principal amount) * ((1+ r(interst rate)/n) ** t(tim period))
# principal = 0
# rate = 0
# time_period = 0

while True :
    principal = float(input("Enter the principle amount : "))
    if principal <= 0 :
         print("Principal Amount cannot be Less than or Equals to Zero")
    else: 
         break
while True : 
    rate = float(input("Enter the rate Amount : "))
    if rate <= 0 :
         print("rate Amount cannot be Less than or Equals to Zero")
    else: 
         break

while True:
    time_period = int(input("Enter the time_period  : "))
    if time_period <0 :
         print("time_period  cannot be Less than")
    else: 
         break

# CI =  # a(final amount)=p (principal amount) * ((1+ r(interst rate)/n) ** t(tim period))
CI = float((principal * (1+ rate/100)**time_period))
print(f"Balance after {time_period} years for {principal} principal amount per {rate} rate of interest is  {CI}")
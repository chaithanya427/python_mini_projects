email=input("Enter your Email Address : ")
index= email.index('@')
username= email[0:index]
domain = email[index +1 :]

print(f"Your username is {username} and Domain is {domain}")
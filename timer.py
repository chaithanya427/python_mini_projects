import time 
t = int(input("time to wait in seconds : "))
for i in range(t,0,-1):
    seconds = i % 60 
    minutes = i // 60
    hours= i //3600

    # print()
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time up")


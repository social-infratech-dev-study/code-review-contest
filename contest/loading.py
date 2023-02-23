import time

print("How many seconds?")
print(">>> ", end="")
n = int(input())

print("loding starts\n")

elapsed = 0
while n > 0:
    elapsed += 1
    sleep(1)
    print("loading... " + elapsed)
    
print("\nloading ends")
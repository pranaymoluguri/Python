import numpy as np

r=np.random.randint(100)
i=0
while i<1:
    x=int(input("Guess the number between 0 and 100 : "))
    if(x==r):
        print("Perfect Catch !!")
        break
    elif(x<r):
        print("Increase the number... ")
    elif(x>r):
        print("Decrease the number...")

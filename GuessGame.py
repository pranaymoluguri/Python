import numpy as np

r=np.random.randint(100)
i=0
c=0
while i<1:
    x=int(input("Guess the number between 0 and 100 : "))
    c+=1
    if(x==r):
        print("Nice Catch !! The number was: ",r,"& No of attempts: ",c)
        break
    elif(x<r):
        print("Increase the number... ")
    elif(x>r):
        print("Decrease the number...")

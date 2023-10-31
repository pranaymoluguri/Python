print("*** WELCOME TO ATM ***")
cash=int(input("Enter the amount (in multiples of 100s only): "))

if (cash%100==0):
    cash2k=int(cash/2000)
    print("2000 x" , cash2k)
    cash=cash%2000
    cash5=int(cash/500)
    print("500 x ", cash5)
    cash=cash%500
    cash1=int(cash/100)
    print("100 x ", cash1)
else:
    print("Multiples of 100 only allowed !!")

print("Thank you !! Visit Again")   

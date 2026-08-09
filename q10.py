CP = int(input("Enter the cost price of the item "))
SP = int(input("Enter the selling price of the item "))

if(SP-CP >  0):
    print("PROFIT!!!! OF :", SP-CP,"RS")

elif(SP-CP == 0):
    print("NOTHING ")

else:
    print("LOSS OF :( ", SP-CP,"RS" )
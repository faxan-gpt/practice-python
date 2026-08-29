num1 = int(input("Enter your first no.")) 
num2 = int(input("Enter your second no. "))

def multiply(a,b): # defiining the function for multiplication
   
    negative = (a<0) ^ (b<0) # performs EXOR operation , if any one is true , negative is true 
    a,b = abs(a), abs(b) # abs gives the absoule value of the variable( no sign , decimal and  shit)

    result = 0 # initializes the result varible from zero
    for _ in range(b): # _ refers to "kch bhi/ jo bhi " in the range(b)
        result += a # increrment result by a evrytime loop works

    if (negative): 
        print (-result)
    else:
        print (result)

multiply(num1,num2) # hee num1 gets equal to a, num2 gets equal to b


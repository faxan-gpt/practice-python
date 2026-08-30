n1=int(input("Enter your first no."))
n2= int(input("Enter your second no."))

for i in range(1,min(n1,n2)+1): # min(n1,n2) used for getting the minimum no. among n1, n2 
    if n1%i==0 and n2%i==0:
        hcf=i
print("The hcf of both  no. is ", hcf)

n1 = int(input("Enter your first no."))
n2 = int(input("Enter your 2nd no. "))


x = []
for i in range(1,n1+1,1):
    if n1%i==0:
        x.append(i)
        print(i)

y  = []
for el in range(1,n2+1,1):
        if n2%el==0:
            y.append(el)
            print(el)

hcf = 0
for factor in x:
     if factor in y and factor > hcf:
          hcf = factor 
print("the hcf of both no. is ", hcf)


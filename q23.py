x = int(input("Enter your 1st no. "))
y = int(input("Enter your 2nd no. "))
z = int(input("Enter your 3rd no. "))

print("This is before swapping",x,y,z)
temp = x
x = y 
y = z
z=temp

print("This is after swapping", x,y,z)

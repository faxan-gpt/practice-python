a = int(input(" Enter the first no. "))
b = int(input("Enter the second no. "))

print (" This is before swapping " ,a,b)

# a,b = b,a 
temp = a
a=b
b=temp

print ("This is after swapping ", a,b )

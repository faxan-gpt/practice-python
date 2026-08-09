a = int(input("Enter your 1st coordinate "))
b = int(input("Enter your 2nd coordinate "))
c = int(input("Enter your 3rd coordinate "))
d = int(input("Enter your 4th coordinate "))

dist = ((a - b)**2 + (c-d)**2)**0.5 # distance formula for 2-D space 
print( " The Euclidean distance between two coordinates is ", dist)
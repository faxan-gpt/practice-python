num =  int(input("Enter the no. of layers you want to print:"))
width = 2*num-1

i = 1
while i <= num:
    stars = 2*i-1 # selects the no. of stars 
    pattern = "*" * stars
    riyal_pattern= pattern.center(width) # chooses the width requirment as per the stars availability
    print(riyal_pattern)
    i += 1


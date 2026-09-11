n = int(input("Enter the no. of rows  : "))
num = 1

for i in range(1, n + 1):
    for j in range(i): # working till i for the cuurrent scenario
        print(num, end=" ")
        num += 1 # acting as counter 
    print()  # move to next line
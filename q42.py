num = int(input("Enter the no. here : "))
 
i = 1 # for initalization
while i < num: 
    pattern  = "*" * i 
    print(pattern)
    i +=1 # increment the variable

pattern = num-1 # assigned the patterned value to numerical value i.e 2
while pattern > 0:
        pattern2 = "*"*pattern
        print(pattern2)
        pattern -= 1 # decrement the pattern variable
sum = 0
count =0 

while True:

    n = float(input("Enter your no. "))
    if n == 0:
        break 
    else:
        sum += n 
        count += 1

avg = sum / count
print(avg)
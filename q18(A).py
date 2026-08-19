num =int(input("Enter your no. "))
power = len(str(num))
sos = 0

og = num # just to save the number 
temp = num # coz we dont perform operations on original no, varibale


while temp > 0:
    dig = temp % 10 # extracting each digits 
    sos += dig**power # sum of square or powered digits
    temp =  temp // 10 # eliminates the non integer part 
    # this loop will run till temp becomes 0 
if sos == og:
    print("it is an armstrong no. ")
else:
    print("it is not an armstrong no.")
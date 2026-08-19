def arm_num(num):
    og = num # to save the no. originally
    temp = num  # to perform the operations on temp coz cant do it on original no.
    power = len(str(num))

    sos = 0
    while temp > 0:
        dig = temp %10 # to access the digits of the number
        sos += dig**power # stores and add to sos 
        temp = temp // 10 # eliminates the non integer term
    return sos == og # we do this coz whenever this function gets called , this can work their by giving true or false value 

num=int(input("Enter your no. "))
if  arm_num(num):
    print(f"{num} is an armstrong no.")
else:
    print(f"{num} is not an armstrong no. ")
    
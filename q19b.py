def nar_num(no):
    real = no
    power = len(str(no))
    fake = no
    sop = 0 # sum of powered no.
    while fake > 0:
        digits = fake % 10 # access the digits of the number
        sop += digits**power
        fake = fake // 10

    return sop == no
no=int(input("Enter your no."))
if nar_num(no):
    print(f"{no} is a narcissist no.")
else:
    print(f"{no} is not a narcissist no. ")
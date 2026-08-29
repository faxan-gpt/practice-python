def prime_or_not(a):
    if a<=1: # prime no. cant be 1 and lower then one
        print(f"{a} is not a prime no.")
        return False
    if a<=3: # 2,3 are prime no.s but 1 is not , which we have already excluded 
        print(f"{a} is a prime no.")
        return True 
    if a%2 == 0: # exclud eall the even no. except 2 , which we have included above
        print(f"{a} is not a prime no.")
        return False

    for i in range(3,int(a**0.5) +1 ,2): """starting from 3 , to stop at "root n" to avoid overhead task , when we go towards "n" ,
                                     after the middle point of the factors of n , factors get repeat which makes the code more redundent , 
                                     we have chosen 2 as our step coz we now want to work for the odd no., 
                                     we have added 1 coz to approximate the value of the a   """  
    if a%i==0: # if any no. from above odd no. divides the a completely then its not a prime no. 
        print(f"{a} is not a prime no. ")
    else:
        print(f"{a} is a prime no. ")

num = int(input("Enter your no.  here : "))
prime_or_not (num)
def gcd(a,b):
    while b: # this is the shorthand for b != 0 
        a,b= b,a%b # this will make the b as 0 , will have value of a only
        return a

def lcm(c,d):
    return (c*d)//gcd(c,d) 

num1=int(input("Enter your first no. "))
num2 = int(input("Enter your second no. "))

result = lcm(num1,num2)

print(f"The lcm of {num1}and {num2} is {result}")
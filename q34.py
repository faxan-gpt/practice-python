def print_prime(n):
    if n<=1:
        return False
    if n<3:
        return True 
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,1):
        if n%i == 0:
            return False
    return True 

count = 0
n = 2

prime=[]

while count<25:
    if print_prime(n):
        prime.append(n)
        count+=1

    n+=1 

print_prime(25)
print(prime)

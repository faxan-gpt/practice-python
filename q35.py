def fib(n):
    a,b = 0,1 
    for _ in range(n):
         a,b= b,a+b # makes a as b  and b as sum of a,b # AKA function for fibonnaci series
    return a 



n = int(input("Enter your no."))
count = 0 # for initalization
while count < n: 
        print((fib(count)))
        count += 1




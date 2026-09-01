def fib(n):
    a,b = 0,1
    for _ in range(n):
         a,b= b,a+b
    return a



n = int(input("Enter your no."))
count = 0 
while count < n:
        print((fib(count)))
        count += 1




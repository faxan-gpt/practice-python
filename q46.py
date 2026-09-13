

def sum_of_fact(n):
    i=1
    fact = 1
    sum = 0
    while i<=n:
        fact *= i
        i+=1 

        sum += i/fact 
        

    print(sum)

sum_of_fact(5)





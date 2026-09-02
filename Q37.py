#def find_value(n):
  #  sum = n + n*n + n*n*n
 #   print(sum)

#find_value(5)

''' The above code is incorrect as per the question's requirment '''

def find_sum(n):
    n1 = int(str(n)*1) #repeat the string once 
    n2 = int(str(n)*2) # repeat the string twice 
    n3 = int(str(n)*3) # repeat the string thrice

    sum = n1+n2+n3

    print(sum)

find_sum(5)
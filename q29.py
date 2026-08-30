
for el in range(100,1001,1):
    
    og = el
    temp = el

    power= len(str(el))
    sos = 0 # its the inital value 

    while temp > 0:
        digits = temp % 10 # gets the digit no.
        sos  += digits**power # its the armstrong no. formula  
        temp = temp //10 # removes the zero we get form temp % 10 

    if (sos == og ):
        print (og)



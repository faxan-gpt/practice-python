def salary( HRA=0.10, DA=0.05,PF=0.03): 
    sal= int(input("Enter your salary: "))
    
    if(500000<= sal <= 1000000):
        tax=0.1
        in_hand= sal*(1-HRA - DA - PF -tax)
        print(in_hand)

    elif(1100000<= sal <= 2000000  ):
        tax=0.2
        in_hand= sal*(1-HRA - DA - PF -tax)
        print(in_hand)
        
    elif(2100000<= sal <= 3000000):
        tax=0.3
        in_hand= sal*(1-HRA - DA - PF -tax)
        print(in_hand)

salary()
salary()
salary()

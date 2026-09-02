def CI(p , r , t, n):
    interest_amount = p*(1+r/n)**n*t

    compound_interest= interest_amount - p

    print(compound_interest)

CI(100000,2 , 3,4)
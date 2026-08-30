num = [1,2,3,4]
for a in num: # works for the first position
    for b in num: # works for 2nd position
        if b==a:
            continue # if above condition gets true , it will skip that part and move on
        for c in num: # works for 3rd postion 
            if c==a or c==b:
                continue# if above condition gets true , it will skip that part and move on
            for d in num: # works for 4th position
                if d == a or d==b or d==c:
                    continue# if above condition gets true , it will skip that part and move on
                print(a,b,c,d)
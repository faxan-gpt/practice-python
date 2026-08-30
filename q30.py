def popul(current , increment , tenure ):
   
    
    while tenure >0:

        now_popul = current*(1-increment)
        tenure -= 1
        current = now_popul
        print (int(now_popul))

popul(10000,0.10,10)
popul(10000,0.10,20)



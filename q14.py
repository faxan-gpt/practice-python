def getangle(s:str)->float: # s:str is saying that the parameter s will be a string , -> float hints (not force ) that the value returning will be float 
 h,m=map(int,s.split(":")) # this split the string of s parameter in integer way

 h = h%12 # converts 24 hrs time to 12 hrs time
 minute_angle = 6*m # angle of minutes hand 
 hour_angle = 30*h + 0.5*m # angle of hour hands

 diff=abs(hour_angle-minute_angle) # gives the absolute diff of both hands
 angle = min(diff,360-diff) #compares both angles and gives the samller output
 return round(angle,3) # rounds off the angle to 3rd deci place

print(f"{getangle("06:00"):.3f}") # output = 180.000
''' "f{..... :.3f" gives the output to the 3rd deccimal place 
getangle(...) runs the above logic code
'''
print(f"{getangle("11:22"):.3f}") #output= 151.000

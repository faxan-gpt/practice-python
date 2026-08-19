num  = int(input("Enter your no. "))

power = len(str(num ))
riyal =  num
sop = 0
phake = num 

while phake > 0:
    digi = phake%10 # separate out each digtis
    sop +=  digi**power # sum of the powered digits 
    phake = phake // 10 # remove the  non integral terms 

if sop == num:
    print(f"{num } is a narcissist no.")
else:
    print(f"{num} is not an narcissist no.")
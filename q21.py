a = "a"
b = "b"
c = "c"
d = "d"

print("a. Cm to Ft")
print("b. Km to miles ")
print("c. Us to Inr  ")
print("d. Exit ")

print ("Choose any one option ")

select=input("Enter your option: ")

while select  != d :
    if(select == a ):
        cm=int(input("Enter your value in cm: "))
        ft= cm/30.48
        print(ft , "ft")

    elif(select == b ):
        km = int(input("Enter the value in km: "))
        miles= km/1.6
        print(miles,"miles" )

    elif(select == c ):
        us=int(input("Enter your us dollar value: "))
        inr = us/95.6
        print(inr, "Rs")

    select=input("Again enter your option: ")

print ("You have now exited the menu")

    
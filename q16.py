temp = int(input("Enter the temperature: "))
hum = int(input("Enter the humidity: "))
if( temp >= 30 and hum >= 90  ):
    print("Hot and humid ")
elif(temp >= 30 and hum < 90):
    print("Hot")
elif(temp < 30 and hum >= 90 ):
    print("Cool and humid ")
elif(temp < 30 and hum < 90 ):
    print("cool")
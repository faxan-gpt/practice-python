
num = int(input("Enter the value of numerator "))
den = int(input("Enter the vallue of denominator "))

import math 

gcd = math.gcd(num, den)
simplified_num = num // gcd
simplified_den = den// gcd

print(f" {simplified_num }/ {simplified_den}")
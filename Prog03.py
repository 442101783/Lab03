def convert_CtoF(n):
    F = 9/5 * float(n) +32
    return F
print("enter temperature in celius")
F = convert_CtoF(input())
print("the temperature in Fahrenheit is ",F)
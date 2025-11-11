a=int(input("Enter first value"))
b=int(input("Enter second value"))
while b!=0:
    temp=a
    b=a%b
    a=temp
print("The GCD is: ",a)

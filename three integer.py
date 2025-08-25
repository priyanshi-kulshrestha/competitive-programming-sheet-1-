a=int(input("enter a  first number"))
b=int(input("enter a second number"))
c=int(input("enter a third number"))
print(a,b,c)
if a>=b and a>=c:
    print("maximum number is:",a)
elif b>=a and b>=c:
    print("maximum number is :",b)
else:
    print("maximum number is:",c)
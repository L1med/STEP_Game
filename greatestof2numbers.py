a = int(input("First number:"))
b = int(input("Second number:"))
c = int(input("Third number:"))
if a == b and a == c:
    print("Same number.")
if b > a and c < b:
    print("The greatest number is "+str(b))
    if a>c:
        print("The middle number is "+str(a))
        print("The least number is "+str(c))
    else:
        print("The middle number is "+str(c))
        print("The least number is "+str(a))
if b < c and a < c:
    print("The greatest number is "+str(c))
    if b>a:
        print("The middle number is "+str(b))
        print("The least number is "+str(a))
    else:
        print("The middle number is "+str(a))
        print("The least number is "+str(b))
if a > b and a > c:
    print("The greatest number is "+str(a))
    if b>c:
        print("The middle number is "+str(2))
        print("The least number is "+str(3))
    else:
        print("The middle number is "+str(3))
        print("The least number is "+str(2))
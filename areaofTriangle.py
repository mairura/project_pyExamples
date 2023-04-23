a = int(input("area with sides(1) or base-height(2) :"))
if a == 2:
    b = int(input("enter the base:"))
    h = int(input("enter the height:"))
    area = float(0.5*b*h)
    print("area is", area)
else:
    s1 = float(input("enter side 1:"))
    s2 = float(input("enter side 2:"))
    s3 = float(input("enter side 3:"))
    s = float((s1+s2+s3)/2)
    area = (s*(s-s1)(s-s2)(s-s3)) ** 0.5
    print("area is", area)

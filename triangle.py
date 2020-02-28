l1 = int(input("Length of side 1: "))
l2 = int(input("Length of side 2: "))
l3 = int(input("Length of side 3: "))
if l3 < l1 + l2 and l1 < l3 + l1 and l2 < l1 + l3:
    if l3==l2==l1:
        result = "Equilateral"
    elif l3==l2 or l1==l2 or l3==l1:
        result = "Isosceles"
    else:
        result = "Scalene"
else:
    result = "Not a triangle"
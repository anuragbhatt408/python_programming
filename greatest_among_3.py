x = int(input(" enter x : "))
y = int(input(" enter y : "))
z = int(input(" enter z : "))
if x>y and x>z:
    print("{} is greater".format(x))
elif y>x and y>z:
    print("{} is greater ".format(y))
else:
    print("{} is greater ".format(z))

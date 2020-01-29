n = int(input("enter the number for factorial "))

fact = 1
for i in range(1,n+1):
    fact = fact*i

print(fact," is factorial of ",n)

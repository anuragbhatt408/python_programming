n = int(input("enter value of n: "))
n1, n2 = 0, 1
count = 0
if n == 1:
   print("Fibo series is",n)
   print(n1)
elif n <= 0:
   print("Fibo series:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

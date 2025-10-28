def facto(num):
    fact = 1
    for i in range(1, num+1):
        fact=fact*i
    return fact

num = int(input("enter number: "))
print(f"factorial of {num} is {facto(num)}")
   
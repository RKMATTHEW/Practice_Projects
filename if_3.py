
Number = 0

User = int(input("enter a number:  "))

if Number == 0:
    Number = (User % 10)
    print(Number)

#or

num = int(input("enter a number:  "))
print("Last digit of number is ", num % 10 )
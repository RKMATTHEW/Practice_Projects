#Number = int(input("enter a number:  "))

#if (Number % 2) == 0:
    #print("This value is positive")
#else:
    #print("This value is negative")



#electricity bill

Unit = int(input("What is the amount of units:  "))
amt = 0

if Unit <= 100:
    amt = 0
    print(amt)
elif Unit >= 100 and Unit <= 100:
    amt = (Unit - 100) * 5
    print(amt)
elif Unit >= 200:
    amt = 500 + (Unit - 200) * 10
    print(amt)



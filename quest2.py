flag = 0
i = 1
sums = 0
passlist = []
faillist = []
distinclist = []

while not (flag == 1):
    inval = float(input("Enter student mark "+str(i)+" : "))

    if inval < 0:
        flag = 1

    else:
        if inval < 50:
            faillist.append(inval)

        elif inval >= 75:
            passlist.append(inval)
            distinclist.append(inval)

        else:
            passlist.append(inval)

    i += 1
    sums += inval

print("\n\n\n")
print("The number of marks entered is : ",(i-1))
print("The average of all the marks is : ",sums/(i-1))
print("The number of fails is : ",len(faillist))
print("The number of passes is : ",len(passlist))
print("The number of distinctions is : ",len(distinclist))

if len(passlist) > 0:
    print("The highest mark is : ",max(passlist))

else:
    print("The highest mark is : ",max(faillist))

if len(faillist) > 0:
    print("The lowest mark is : ",min(faillist))

else:
    print("The lowest mark is : ",min(passlist))

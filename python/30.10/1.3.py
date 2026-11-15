a = int(input(""))

for j in range(a):
    for i in range (a):
        if j == 0 or j == a - 1 or i == 0 or i == a - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
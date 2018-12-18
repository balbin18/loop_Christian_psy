def toRomanNum(x):
    if x <= 200:
        if x == 200:
            print("CC", end="")
        elif x < 200 and x > 100:
            print("C", end="")
            a = x - 100
            toRomanNum(a)
        elif x == 99:
            print("IC", end="")
        elif x <= 98 and x >= 50:
            print("L", end="")
            a = x - 50
            toRomanNum(a)
        elif x == 49:
            print("IL", end="")
        elif x <= 48 and x >= 40:
            print("XL", end="")
            a = x - 40
            toRomanNum(a)
        elif x <= 39 and x >= 10:
            print("X", end="")
            a = x - 10
            toRomanNum(a)
        elif x <= 9 and x >= 5:
            print("V", end="")
            a = x - 5
            toRomanNum(a)
        elif x < 5 and x > 0:
            print("I", end="")
            a = x - 1
            toRomanNum(a)
        else:
            print()

toRomanNum(80)

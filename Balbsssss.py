for x in range(1, 11):
    for y in range(1, 11):
       hue = x * y

       if hue % 2 == 0:
           print ("e", end = '\t')
       else:
           print(x*y, end = '\t')
    print()

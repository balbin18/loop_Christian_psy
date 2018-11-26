pangalan = input ("Enter your Name:")
pangalan_palit_2 = ""

for x in range(len(pangalan)):
   char = pangalan[x]


   if char == "A":
       pangalan_palit_2 += "B"
   elif char == "B":
      pangalan_palit_2+= "C"
   elif char == "C":
       pangalan_palit_2 += "D"
   elif char == "D":
       pangalan_palit_2+= "E"
   elif char == "E":
       pangalan_palit_2+= "F"
   elif char == "F":
      pangalan_palit_2 += "G"
   elif char == "G":
       pangalan_palit_2+= "H"
   elif char == "H":
      pangalan_palit_2 += "I"
   elif char == "I":
      pangalan_palit_2 += "J"
   elif char == "J":
       pangalan_palit_2 += "K"
   elif char == "K":
       pangalan_palit_2+= "L"
   elif char == "L":
      pangalan_palit_2+= "M"
   elif char == "M":
       pangalan_palit_2 += "N"
   elif char == "N":
       pangalan_palit_2 += "O"
   elif char == "O":
      pangalan_palit_2 += "P"
   elif char == "P":
      pangalan_palit_2 += "Q"
   elif char == "Q":
      pangalan_palit_2+= "R"
   elif char == "R":
     pangalan_palit_2 += "S"
   elif char == "S":
     pangalan_palit_2 += "T"
   elif char == "T":
     pangalan_palit_2 += "U"
   elif char == "U":
      pangalan_palit_2 += "V"
   elif char == "V":
      pangalan_palit_2 += "W"
   elif char == "W":
     pangalan_palit_2+= "X"
   elif char == "X":
     pangalan_palit_2 += "Y"
   elif char == "Y":
     pangalan_palit_2 += "Z"
   else:
     pangalan_palit_2 += char

print(pangalan_palit_2)

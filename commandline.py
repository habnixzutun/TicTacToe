liste = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
test_tuple = tuple()


def show():
      print(f"| {liste[0]} | {liste[1]} | {liste[2]} |\n"
            f"| {liste[3]} | {liste[4]} | {liste[5]} |\n"
            f"| {liste[6]} | {liste[7]} | {liste[8]} |\n")


while True:
      show()
      try:
            temp = eval(input("Wo:\t\t"))
            sign = input("X oder O:\t").lower()
            if type(temp) == type(test_tuple) and len(temp) == 2 and sign == "x" or sign == "o":
                  place = temp[0]-1 + (temp[1]-1)*3
                  if liste[place] == " ":
                        liste[place] = sign
                  else:
                        print("Dieses Feld ist nicht mehr frei")
      except:
            pass

      if liste[0] == "x" and liste[1] == "x" and liste[2] == "x" or\
            liste[3] == "x" and liste[4] == "x" and liste[5] == "x" or\
            liste[6] == "x" and liste[7] == "x" and liste[8] == "x" or\
            liste[0] == "x" and liste[3] == "x" and liste[6] == "x" or\
            liste[1] == "x" and liste[4] == "x" and liste[7] == "x" or\
            liste[2] == "x" and liste[5] == "x" and liste[8] == "x" or\
            liste[0] == "x" and liste[4] == "x" and liste[8] == "x" or \
            liste[2] == "x" and liste[4] == "x" and liste[6] == "x":
            show()
            print("X hat gewonnen")
            break

      if liste[0] == "o" and liste[1] == "o" and liste[2] == "o" or \
            liste[3] == "o" and liste[4] == "o" and liste[5] == "o" or \
            liste[6] == "o" and liste[7] == "o" and liste[8] == "o" or \
            liste[0] == "o" and liste[3] == "o" and liste[6] == "o" or \
            liste[1] == "o" and liste[4] == "o" and liste[7] == "o" or \
            liste[2] == "o" and liste[5] == "o" and liste[8] == "o" or \
            liste[0] == "o" and liste[4] == "o" and liste[8] == "o" or \
            liste[2] == "o" and liste[4] == "o" and liste[6] == "o":
            show()
            print("O hat gewonnen")
            break

input("\nDücke eine beliebige Taste um das Programm zu schließen")

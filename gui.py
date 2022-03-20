from tkinter import *


def click(button):
      global player
      global won
      global lost
      global frame_top
      global frame_bottom
      print(button, won, lost)

      if (not won) and (not lost) and (liste[button] == ""):
            liste[button] = player
            player = players[(players.index(player) + 1) % 2]
            update_frame_top()
            update_frame_main()
            update_frame_botton()

            if liste[0] == "X" and liste[1] == "X" and liste[2] == "X" or\
                  liste[3] == "X" and liste[4] == "X" and liste[5] == "X" or\
                  liste[6] == "X" and liste[7] == "X" and liste[8] == "X" or\
                  liste[0] == "X" and liste[3] == "X" and liste[6] == "X" or\
                  liste[1] == "X" and liste[4] == "X" and liste[7] == "X" or\
                  liste[2] == "X" and liste[5] == "X" and liste[8] == "X" or\
                  liste[0] == "X" and liste[4] == "X" and liste[8] == "X" or \
                  liste[2] == "X" and liste[4] == "X" and liste[6] == "X":
                  won = True
                  print("X hat gewonnen")

            if liste[0] == "O" and liste[1] == "O" and liste[2] == "O" or \
                  liste[3] == "O" and liste[4] == "O" and liste[5] == "O" or \
                  liste[6] == "O" and liste[7] == "O" and liste[8] == "O" or \
                  liste[0] == "O" and liste[3] == "O" and liste[6] == "O" or \
                  liste[1] == "O" and liste[4] == "O" and liste[7] == "O" or \
                  liste[2] == "O" and liste[5] == "O" and liste[8] == "O" or \
                  liste[0] == "O" and liste[4] == "O" and liste[8] == "O" or \
                  liste[2] == "O" and liste[4] == "O" and liste[6] == "O":
                  won = True
                  print("O hat gewonnen")
      if "" not in liste:
            lost = True

      if won:
            frame_top.destroy()

            label = Label(frame_bottom, text=f"{players[(players.index(player) + 1) % 2]} hat gewonnen", font=("Calibri", 30), bg="white")
            label.grid(row=0, column=0)

            button = Button(frame_bottom, text="Neu starten", font=("Calibri", 15), fg="white", bg="black", command=restart)
            button.grid(row=1, column=0)

      elif lost:
            frame_top.destroy()

            label = Label(frame_bottom, text=f"Niemand hat gewonnen", font=("Calibri", 30))
            label.grid(row=0, column=0)

            button = Button(frame_bottom, text="Neu starten", font=("Calibri", 15), fg="white", bg="black", command=restart)
            button.grid(row=1, column=0)


def update_frame_top():
      global frame_top
      global player
      global won
      if not won:
            frame_top.destroy()
            frame_top = Frame(main, bg="white")
            frame_top.pack(pady=20)
            label = Label(frame_top, text=f"{player} ist dran", font=("Calibri", 30), bg="white")
            label.grid()


def update_frame_main():
      global liste
      global frame_main
      frame_main.destroy()
      frame_main = Frame(main, bg="black")
      frame_main.pack(pady=20)

      height = 1
      width = 4
      padx = 5
      pady = 5

      b1 = Button(frame_main, text=liste[0], height=height, width=width, font=("Calibri", 60), command=lambda: click(0))
      b1.grid(row=0, column=0, padx=padx, pady=pady)

      b2 = Button(frame_main, text=liste[1], height=height, width=width, font=("Calibri", 60), command=lambda: click(1))
      b2.grid(row=0, column=1, padx=padx, pady=pady)

      b3 = Button(frame_main, text=liste[2], height=height, width=width, font=("Calibri", 60), command=lambda: click(2))
      b3.grid(row=0, column=2, padx=padx, pady=pady)

      b4 = Button(frame_main, text=liste[3], height=height, width=width, font=("Calibri", 60), command=lambda: click(3))
      b4.grid(row=1, column=0, padx=padx, pady=pady)

      b5 = Button(frame_main, text=liste[4], height=height, width=width, font=("Calibri", 60), command=lambda: click(4))
      b5.grid(row=1, column=1, padx=padx, pady=pady)

      b6 = Button(frame_main, text=liste[5], height=height, width=width, font=("Calibri", 60), command=lambda: click(5))
      b6.grid(row=1, column=2, padx=padx, pady=pady)

      b7 = Button(frame_main, text=liste[6], height=height, width=width, font=("Calibri", 60), command=lambda: click(6))
      b7.grid(row=2, column=0, padx=padx, pady=pady)

      b8 = Button(frame_main, text=liste[7], height=height, width=width, font=("Calibri", 60), command=lambda: click(7))
      b8.grid(row=2, column=1, padx=padx, pady=pady)

      b9 = Button(frame_main, text=liste[8], height=height, width=width, font=("Calibri", 60), command=lambda: click(8))
      b9.grid(row=2, column=2, padx=padx, pady=pady)


def update_frame_botton():
      global frame_bottom
      frame_bottom.destroy()
      frame_bottom = Frame(bg="white")
      frame_bottom.pack()


def restart():
      global won
      global lost
      global players
      global player
      global liste
      won = False
      lost = False
      players = ["X", "O"]
      player = players[0]
      liste = ["", "", "", "", "", "", "", "", ""]

      update_frame_top()
      update_frame_main()
      update_frame_botton()


main = Tk()
main.geometry("650x700")
main.resizable(width=False, height=False)
main.title("TicTacToe")
main.iconbitmap("empty.ico")
main.config(bg="white")


frame_top = Frame(main, bg="white")
frame_top.pack()
frame_main = Frame(main)
frame_main.pack()
frame_bottom = Frame(main, bg="white")
frame_bottom.pack()
restart()


print("gui fertig")

main.mainloop()

print("fertig")

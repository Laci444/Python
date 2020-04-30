import os


class TicTacToe:
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    draw = False
    play = True

    def pick(self, player):
        curr_pick = tuple(input("koordináták egyben: "))
        if curr_pick == ("e", "n", "d"):
            self.endgame()
            print("megvan")
        self.board[int(curr_pick[0]) - 1][int(curr_pick[1]) - 1] = player

    def check(self, player):
        win = None
        count = 0
        draw = True
        for i in self.board:
            for f in i:
                if f == " ":
                    draw = False
                    print(draw)
        print(f"asdf {draw}")
        if draw:
            print("lédksyfjvopsdfv " + draw)
            print(win)
            return win
        for i in self.board:
            if i == [player, player, player]:
                win = True
        for i in range(3):
            col = 0
            for f in range(3):
                if self.board[f][i] == player:
                    count += 1
            if count == 3:
                win = True
                count = 0
        for i in range(3):
            if self.board[i][i] == player:
                count += 1
            if count == 3:
                win = True
                count = 0
        return win

    def display(self):
        os.system("cls")
        x = 0
        print()
        for i in self.board:
            print("\t", end="")
            print(i[0], i[1], i[2], sep="  |  ")
            x += 1
            if x < 3:
                print("       ---------------")
        print()

    def endgame(self, state="end"):  # TODO nem működik van vele valami TOFIX!
        if not state == "end":
            print("bnt van")
            print(f"A játéknak vége! {state} győzött")
            self.play = False
            print(self.play)

    def __init__(self):  # TODO: implemented draw; nem működik .-.
        self.display()
        winner = None
        while self.play:
            try:
                print("O választ")
                self.pick("O")
                print(self.play)
                if not self.play: break
            except IndexError:
                print("Helytelen formátum!")
                continue
            except ValueError:
                print("Csak számokat adhatsz meg!")
                continue
            else:
                pass
                if self.play:
                    self.display()
                    if self.check("O"): self.endgame("O")
                    elif self.check("O") is None: self.endgame("draw"); print("alma ", self.check("O")) ; break
            try:
                print("X választ")
                self.pick("X")
                if not self.play: break
            except IndexError:
                print("Helytelen formátum!")
                continue
            except ValueError:
                print("Csak számokat adhatsz meg!")
                continue
            else:
                if self.play:
                    self.display()
                    if self.check("X"):
                        self.endgame("X")
                    elif self.check("X") is None:
                        self.endgame("draw")


if __name__ == "__main__":
    game = TicTacToe()

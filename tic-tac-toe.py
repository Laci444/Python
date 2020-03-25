import os


class TicTacToe:
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    play = True

    def pick(self, player):
        curr_pick = tuple(input("koordináták egyben: "))
        print(curr_pick)
        if curr_pick == ("e", "n", "d"):
            self.endgame()
        self.board[int(curr_pick[0]) - 1][int(curr_pick[1]) - 1] = player

    def check(self, player):
        win = None
        count = 0
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
        if state is not "end":
            print(f"A játéknak vége! {state} győzött")
            self.play = False

    def __init__(self):
        self.display()
        winner = None
        while self.play:
            try:
                print("O választ")
                self.pick("O")
                if self.play is False: break
            except IndexError:
                print("Helytelen formátum!");
                continue
            except ValueError:
                print("Csak számokat adhatsz meg!");
                continue
            else:
                self.display()
                if self.check("O"): winner = "O"; self.endgame(winner)
            try:
                print("X választ")
                self.pick("X")
                if self.play is False: break
            except IndexError:
                print("Helytelen formátum!");
                continue
            except ValueError:
                print("Csak számokat adhatsz meg!");
                continue
            else:
                self.display()
                if self.check("X"): winner = "X"; self.endgame(winner)


if __name__ == "__main__":
    game = TicTacToe()

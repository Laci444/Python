import os


class TicTacToe:
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    def pick_X(self):
        curr_pick = tuple(input("koordináták egyben: "))
        self.board[int(curr_pick[0]) - 1][int(curr_pick[1]) - 1] = "X"

    def pick_O(self):
        curr_pick = tuple(input("koordináták egyben: "))
        self.board[int(curr_pick[0]) - 1][int(curr_pick[1]) - 1] = "O"

    def check(self, player):
        win = None
        col = 0  # TODO: hiányzik az átlós ellenőrzés
        for i in self.board:
            if i is [player, player, player]:
                win = True
        for i in range(3):
            col = 0
            for f in range(3):
                if self.board[f][i] == player:
                    col += 1
            if col == 3:
                win = True
                break
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

    def __init__(self):
        self.display()
        winner = None
        while True:
            print("O választ")
            self.pick_O()
            self.display()
            if self.check("O"): winner = "O"; break  # TODO: csak X tud nyerni meg kell oldani
            print("X választ")
            self.pick_X()
            self.display()
            if self.check("X"): winner = "X"; break
        print(f"A játéknak vége! {winner} győzött")


if __name__ == "__main__":
    game = TicTacToe()

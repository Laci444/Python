import random


class Password:
    letters = "qwertzuopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM"
    symbols = "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
    endpass = ""

    def gen(self, level=1):
        prepass = []
        rnl = lambda: random.choice(self.letters)
        upper = lambda: random.randrange(2)
        rns = lambda: random.choice(self.symbols)
        rnn = lambda: random.randrange(10)
        flip = lambda: random.randrange(3)

        if level == 1:
            for i in range(8):
                if upper() == 0:
                    prepass.append(rnl())
                elif upper() == 1:
                    prepass.append(str(rnn()))
        elif level == 2:
            for i in range(8):
                if flip() == 0:
                    prepass.append(rnl())
                elif flip() == 1:
                    prepass.append(rns())
                else:
                    prepass.append(str(rnn()))
        elif level == 3:
            for i in range(16):
                if flip() == 0:
                    prepass.append(rnl())
                elif flip() == 1:
                    prepass.append(rns())
                else:
                    prepass.append(str(rnn()))
        else:
            print("Ilyen fokozatú jelszó nincs!")
        self.endpass = "".join(prepass)


mypass = Password()
print("Üdv! Ez egy jelszó generátor. 1-től 3-ig adhatsz meg jelszó erősségeket.")
try:
    mypass.gen(int(input()))
    print("A jelszavad elkészült:")
    print(f"\t {mypass.endpass}")
except:
    print("Csak szám formátumú fokozatok léteznek!")

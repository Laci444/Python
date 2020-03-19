words_onenumber = {
    "1" : "one",
    "2" : "two",
    "3": "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eigth",
    "9" : "nine",
}
words_twonumber = {
    "1" : "ten",
    "2" : "twenty",
    "3" : "thirty",
    "4" : "forty",
    "5" : "fifty",
    "6" : "sixty",
    "7" : "seventy",
    "8" : "eighty",
    "9" : "ninety"
}

def egyes(szam):
    return words_onenumber[szam[0]]
def tizes(szam):
    return words_twonumber[szam[0]], egyes(tuple("".join(szam)[1:]))
def szazas(szam):
    return (words_onenumber[szam[0]], "hundred") + tizes(tuple("".join(szam)[1:]))
def ezres(szam):
    return (words_onenumber[szam[0]], "thousand") + szazas(tuple("".join(szam)[1:]))
def tizezer(szam):
    return (words_twonumber[szam[0]],) + ezres(tuple("".join(szam)[1:]))
def szazezer(szam):
    return (words_onenumber[szam[0]], "hundred") + tizezer(tuple("".join(szam)[1:]))
def millio(szam):
    return (words_onenumber[szam[0]], "million") + szazezer(tuple("".join(szam)[1:]))
def tizmillio(szam):
    return (words_twonumber[szam[0]],) + millio(tuple("".join(szam)[1:]))
def milliard(szam):
    return (words_onenumber[szam[0]], "billion") + tizmillio(tuple("".join(szam)[1:]))


def do_the_magic(numbers):
    lenght_of_numbers = len(numbers)
    if lenght_of_numbers == 1:
        return egyes(numbers)
    elif lenght_of_numbers == 2:
        return tizes(numbers)
    elif lenght_of_numbers == 3:
        return szazas(numbers)
    elif lenght_of_numbers == 4:
        return ezres(numbers)
    elif lenght_of_numbers == 5:
        return tizezer(numbers)
    elif lenght_of_numbers == 6:
        return szazezer(numbers)
    elif lenght_of_numbers == 7:
        return millio(numbers)
    elif lenght_of_numbers == 8:
        return tizmillio(numbers)
    elif lenght_of_numbers == 9:
        return milliard(numbers)


print(" ".join(do_the_magic(tuple(input("Írd ide a számot: ")))).title())

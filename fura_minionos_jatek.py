def minion_game(string):
    # string.find(subs,)
    vowels = "AEUIO"
    kevin, stuart = 0, 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevin += (len(string) - i)
        else:
            stuart += (len(string) - i)

    if kevin > stuart:
        print("Kevin " + str(kevin))
    elif kevin < stuart:
        print("Stuart " + str(stuart))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
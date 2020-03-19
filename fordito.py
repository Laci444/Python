

translater = "".join(list(map(lambda w: "g" if w.lower() in "aeuioöüóőúűéáí" else w, list(input("Írj ide valamit: ")))))


if __name__ == "__main__":
    print(translater)


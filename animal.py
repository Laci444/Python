noise = str(input())
noise = noise.replace(" ", ", ")
noise = noise.split(", ")
animal = []
counter = 0


def animals(args):
    switch = {
        "Grr": "Lion",
        "Rawr": "Tiger",
        "Ssss": "Snake",
        "Chirp": "Bird"
    }
    return switch.get(args)


for i in noise:
    animal.append(animals(noise[counter]))
    counter += 1

print(" ".join(animal))

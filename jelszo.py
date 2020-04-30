def tobits(s: object) -> object:
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


"""def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)
"""


def bits2str(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)] * 8))


def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)


pw = input()
code = tobits(pw)  #konvertálás bitsorozattá
print(code)
asd = magic(code)  #list -> number
print(asd)
asd = asd >> 4  #bitwise change
print(asd)
#asd = [int(x) for x in str(asd)]   #number -> list
print(type(asd))
x = 101110000101010111000
print(bits2str(str(x)))
print(type(x))
pw = bits2str(str(asd))
print(pw)
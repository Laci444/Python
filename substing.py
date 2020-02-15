# példa: AABCAAADA 3


def merge_the_tools(string, k):
    subint = 3
    for i in range(k):
        subs = string[subint-3:subint]  # AAB
        ismetlo = []
        done = ""
        for curr in subs:
            if curr not in ismetlo:
                done += curr
                ismetlo.append(curr)
        print(done)  # új sorba a maradék
        subint += 3


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# sting / k -> int van -> ha == akkor del -> print

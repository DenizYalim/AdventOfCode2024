import re

with open("input", "r") as file:
    blocks = file.read().split("\n\n")
    totalCoins = 0
    for block in blocks:
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
        px += 10000000000000
        py += 10000000000000
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            print(ca, cb)
            totalCoins += ca*3 + cb
    print(int(totalCoins))

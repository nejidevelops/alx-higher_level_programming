#!/usr/bin/python3
i = 0
for j in range(ord('z'), ord(a) -1, -1):
    print("{}".format(chr(j - i)), end="")
    i = 32 if i == 0 else 0

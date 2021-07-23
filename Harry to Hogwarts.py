n = input()
c = 1
while True:
    x = int("".join(sorted(n,reverse=True)))
    y = int("".join(sorted(n)))
    n = str(x-y)
    if n == '6174':
        break
    else:
        c += 1
print(c)

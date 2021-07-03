t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(0)
    else:
        b = bin(n)[3:].replace('0', '1')
        print(int(b, 2))
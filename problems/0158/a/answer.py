n, k = map(int, input().split())
a = list(map(int, input().split()))

print(len(list(filter(lambda _a: _a > 0 and _a >= a[k - 1], a))))
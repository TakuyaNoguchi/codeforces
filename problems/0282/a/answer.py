ans = 0

for _ in range(int(input())):
    if '++' in input():
        ans += 1
    else:
        ans -= 1

print(ans)
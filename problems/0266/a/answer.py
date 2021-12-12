n = int(input())
s = input()
ans = cnt = 0
head = s[0]

for i in range(1, n):
    if s[i] == head:
        cnt += 1
    else:
        if cnt and s[i] == head: cnt -= 1

        head = s[i]

print(max(ans, cnt))
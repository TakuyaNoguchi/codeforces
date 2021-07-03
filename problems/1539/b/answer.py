n, q = map(int, input().split())
s = input().rstrip()
c_sum = [0]
for i, char in enumerate(s):
    c_sum.append(c_sum[i] + ord(char) - 96)

for _ in range(q):
    l, r = map(int, input().split())

    print(c_sum[r] - c_sum[l - 1])
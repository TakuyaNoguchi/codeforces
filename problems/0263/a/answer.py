row_index = column_index = None

for i in range(5):
    j = next((_j for _j, c in enumerate(input().split()) if c == '1'), -1)

    if j != -1:
        row_index, column_index = i, j
        break

print(abs(row_index - 2) + abs(column_index - 2))
ls = [2, 1, 5, 7, 3]
print(ls)

for i in range(len(ls) - 1):
    for j in range(i, len(ls) - 1):
        if ls[j] > ls[j+1]:
            temp = ls[j]
            ls[j] = ls[j + 1]
            ls[j + 1] = temp
print(ls)
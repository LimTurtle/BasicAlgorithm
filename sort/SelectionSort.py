ls = [2, 1, 5, 7, 3]
print(ls)

for i in range(len(ls)):
    minNum = ls[i]
    minIdx = i
    for j in range(i, len(ls)):
        if ls[j] < minNum:
            minNum = ls[j]
            minIdx = j
    ls[minIdx] = ls[i]
    ls[i] = minNum

print(ls)
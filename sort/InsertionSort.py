ls = [2, 1, 5, 7, 3]
print(ls)

for i in range(len(ls)):
    if i+1 == len(ls):
        break
    keyIdx = i+1
    for j in range(keyIdx, 0, -1):
        if ls[j] < ls[j-1]:
            temp = ls[j]
            ls[j] = ls[j-1]
            ls[j-1] = temp
        else:
            break

print(ls)
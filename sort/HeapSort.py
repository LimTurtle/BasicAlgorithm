def makeHeap(ls, index):
    curIdx = index
    while curIdx > 1:
        if ls[curIdx] > ls[curIdx // 2]:
            temp = ls[curIdx]
            ls[curIdx] = ls[curIdx // 2]
            ls[curIdx // 2] = temp
            curIdx = curIdx // 2
        else:
            break

def heapify(ls, index, maxIndex):
    curIdx = index
    compareIndex = -1
    if index > maxIndex or curIdx*2 > maxIndex:
        return
    if curIdx*2 + 1 > maxIndex:
        compareIndex = curIdx*2
    else:
        if ls[curIdx*2] > ls[curIdx*2 + 1]:
            compareIndex = curIdx*2
        else:
            compareIndex = curIdx*2 + 1

    if ls[curIdx] < ls[compareIndex]:
        temp = ls[curIdx]
        ls[curIdx] = ls[compareIndex]
        ls[compareIndex] = temp

    heapify(ls, compareIndex, maxIndex)



ls = [-1, 2, 1, 5, 7, 3]
print(ls)

for i in range(2, len(ls)):
    makeHeap(ls, i)

for i in range(len(ls) - 1, 0, -1):
    temp = ls[1]
    ls[1] = ls[i]
    ls[i] = temp
    heapify(ls, 1, i-1)

print(ls)
def swap(ls, a, b):
    temp = ls[a]
    ls[a] = ls[b]
    ls[b] = temp

def quickSort(ls, start, end):
    print("Start: {} | End: {} | List: {}".format(start, end, ls))
    if start >= end:
        return
    elif end - start == 1 and ls[start] > ls[end]:
        swap(ls, start, end)
        return

    piv = ls[start]
    s = start + 1
    e = end
    left = s
    right = end
    while 1:
        while ls[left] < piv and left < e:
            left += 1
        if left == e:
            if piv <= ls[e]:
                quickSort(ls, start, e-1)
                return
            else:
                quickSort(ls, start+1, e)
                return
        else:
            while ls[right] > piv:
                if left >= right and left == s:
                    quickSort(ls, s, e)
                    return
                elif left >= right:
                    swap(ls, left-1, start)
                    quickSort(ls, start, left-2)
                    quickSort(ls, left, e)
                    return
                right -= 1
            swap(ls, left, right)

ls = [2, 1, 5, 7, 3]
print(ls)

quickSort(ls, 0, len(ls)-1)

print(ls)
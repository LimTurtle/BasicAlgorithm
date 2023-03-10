import sys

ls = [2, 1, 5, 7, 3]
print(ls)

ls.sort()

inp = int(sys.stdin.readline().rstrip())
low = 0
high = len(ls) - 1

while low <= high:
    mid = (low + high) // 2
    if inp > ls[mid]:
        low = mid + 1
        continue
    elif inp < ls[mid]:
        high = mid - 1
        continue
    else:
        print("Find Index: {}".format(mid))
        break

if low > high:
    print("Not Found")
import sys

n, m = map(int, sys.stdin.readline().split())
trees = sorted(map(int, sys.stdin.readline().split()))

start = trees[-1]
end = 0
flag = True

while start >= end:
    mid = (start + end) // 2
    height = sum([i - mid for i in trees if i > mid])
    if height == m:
        print(mid)
        flag = False
        break
    if height > m:
        end = mid + 1
    else:
        start = mid - 1
if flag:
    print(start)

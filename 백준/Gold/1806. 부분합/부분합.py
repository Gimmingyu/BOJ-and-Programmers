import sys

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))


count = 2147483647
flag = 0
current_sum = 0
start, end = 0, 0

while 1:
    if current_sum >= s:
        flag = 1
        count = min(count, end - start)
        current_sum -= numbers[start]
        start += 1
    elif end == n:
        break
    else:
        current_sum += numbers[end]
        end += 1
if flag == 0:
    print(0)
else:
    print(count)

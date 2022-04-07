import sys

test_case = int(sys.stdin.readline())
answer = []
for test in range(test_case):
    a, b = map(int, sys.stdin.readline().split())
    lst_a = sorted(map(int, sys.stdin.readline().split()))
    lst_b = sorted(map(int, sys.stdin.readline().split()))

    count = 0
    for i in lst_a:
        start = 0
        end = len(lst_b) - 1
        while start <= end:
            mid = (start + end) // 2
            if i > lst_b[mid]:
                start = mid + 1
            else:
                end = mid - 1
        count += end + 1
    answer.append(count)

for k in answer:
    print(k)

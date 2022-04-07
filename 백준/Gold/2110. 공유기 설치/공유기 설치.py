import sys

n, c = map(int, sys.stdin.readline().split())
arr = sorted(int(sys.stdin.readline()) for i in range(n))

start = 0
end = arr[-1] - arr[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    target = arr[0]
    router = 1

    for i in range(1, len(arr)):
        if arr[i] >= target + mid:
            target = arr[i]
            router += 1

    if router >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)

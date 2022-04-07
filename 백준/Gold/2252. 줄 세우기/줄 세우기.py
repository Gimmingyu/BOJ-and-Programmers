from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
entry_level = [0] * (n + 1)
queue = deque()

for i in range(m):
    front, back = map(int, sys.stdin.readline().split())
    graph[front].append(back)
    entry_level[back] += 1

for student in range(1, n + 1):
    if entry_level[student] == 0:
        queue.append(student)


def bfs(q: deque):
    while q:
        f = q.popleft()
        yield f
        for b in graph[f]:
            entry_level[b] -= 1
            if entry_level[b] == 0:
                q.append(b)


for ans in bfs(queue):
    print(ans, end= " ")

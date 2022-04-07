import time


def n_queen(row):
    global count
    if row == n:
        count += 1
        return

    for col in range(n):
        flag = True

        for i in range(row):

            if solve[i] == col or row - i == abs(col - solve[i]):
                flag = False
                break

        if flag:
            solve[row] = col
            n_queen(row + 1)


n = int(input())
# start = time.time()
solve = [0] * n
count = 0
n_queen(0)
# print(time.time() - start)
print(count)

# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

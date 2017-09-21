# https://www.hackerrank.com/challenges/is-fibo
# Binot Formula using golden ratio
from math import sqrt

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    plusSol = sqrt(5 * N * N + 4) % 1 == 0
    minusSol = sqrt(5 * N * N - 4) % 1 == 0
    if plusSol or minusSol:
        print('IsFibo')
    else:
        print('IsNotFibo')

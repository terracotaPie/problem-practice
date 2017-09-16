# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

from collections import Counter


def number_needed(a, b):
    a_c = Counter(a)
    b_c = Counter(b)
    return sum((b_c - a_c).values()) + sum((a_c - b_c).values())

  
X = input().strip()
Y = input().strip()

print(number_needed(X, Y))

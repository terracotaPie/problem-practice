# https://www.hackerrank.com/challenges/ctci-contacts/problem

class Node:
    children = [0, dict()]  # (count, children)

    def __init__(self):
        pass

    def add(self, name):
        curr_node = self.children
        for char in name:
            if char not in curr_node[1].keys():
                # Didn't find the match
                curr_node[1][char] = [0, dict()]
            curr_node[0] += 1
            curr_node = curr_node[1][char]
        curr_node[0] += 1

    def find(self, partial_name):
        curr_node = self.children
        for char in partial_name:
            if char not in curr_node[1].keys():
                return 0
            curr_node = curr_node[1][char]
        return curr_node[0]


root = Node()

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        root.add(contact)
    elif op == 'find':
        print(root.find(contact))


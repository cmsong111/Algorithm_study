import sys


def preorder(root):
    if root != '.':
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])


def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")


tree = {}
nodecount = int(sys.stdin.readline().rstrip())

for i in range(nodecount):
    root, right, left = map(str, sys.stdin.readline().split())
    tree[root] = [right, left]

print(tree)

preorder('A')
print()
inorder('A')
print()
postorder('A')

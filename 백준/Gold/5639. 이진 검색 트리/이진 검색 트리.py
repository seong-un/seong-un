import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline

def front_to_back(tree):
    if len(tree) == 1:
        return [tree[0]]
    elif len(tree) == 0:
        return []
    root = tree[0]
    for i in range(1, len(tree)):
        if tree[i] > root:
            return front_to_back(tree[1:i]) + front_to_back(tree[i:]) + [root]
    return front_to_back(tree[1:]) + [root]

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

for i in front_to_back(tree):
    print(i)
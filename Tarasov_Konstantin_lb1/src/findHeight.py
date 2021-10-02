from src.findDepth import findDepth


# Нахождение высоты дерева
def findHeight(parent, n):
    depth = [0] * n

    for i in range(n):
        findDepth(parent, i, depth)

    m = depth[0]
    for i in range(1, n):
        if depth[i] > m:
            m = depth[i]

    return m

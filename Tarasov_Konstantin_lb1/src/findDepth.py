# Нахождение высоты узла дерева
def findDepth(parent, i, depth):
    if parent[i] == -1:
        depth[i] = 1
        return

    if depth[i] != 0:
        return

    if depth[parent[i]] == 0:
        findDepth(parent, parent[i], depth)

    if depth[parent[i]] != 0:
        depth[i] = depth[parent[i]] + 1
        return

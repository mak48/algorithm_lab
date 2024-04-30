# алгоритм на дереве

def build_tree(l, r):
    node = Node(l, r)
    if l+ 1 < r:
        mid = (r + l)//2
        node.left = build_tree(l, mid)
        node.right = build_tree(mid, r)
    return node

def copy(node, v):
    new_node = Node(node.left_border, node.right_border)
    new_node.value = node.value + v
    new_node.left = node.left
    new_node.right = node.right
    return new_node

def copy_not(node):
    new_node = Node(node.left_border, node.right_border)
    new_node.value = node.value
    return new_node

def change_tree(node, l, r, val):
    if l <= node.left_border and node.right_border <= r:
        return copy(node, val)
    if r <= node.left_border or node.right_border <= l:
        return node
    new_node = copy_not(node)
    new_node.left = change_tree(node.left, l, r, val)
    new_node.right = change_tree(node.right, l, r, val)
    return new_node

def find(node, key):
    if not node.right and not node.left:
        return node.value
    mid = (node.right_border + node.left_border)//2
    if key < mid:
        return node.value + find(node.left, key)
    return node.value + find(node.right, key)

def search(arr, key):
    if key<arr[0] or key>arr[-1]:
        return -1
    l, r = 0, len(arr)
    while r-l > 1:
        mid = (r + l) // 2
        if arr[mid] >= key:
            r = mid
        else:
            l = mid
    if arr[r] == key:
        return r
    return l

class Node:
    def __init__(self, left=None, right=None):
        self.left_border, self.right_border = left, right
        self.left, self.right = None, None
        self.value = 0

def prepare_tree(n):
    if n!=0:
        f = open("прямоугольники.txt", "r")
        modif = []
        xlist, ylist = set(), set()
        for i in range(n):
            p = [int(x) for x in f.readline().split()]
            xlist.add(p[0])
            xlist.add(p[2])
            ylist.add(p[1])
            ylist.add(p[3])
            modif.append([p[1], p[0], p[2], 1])
            modif.append([p[3], p[0], p[2], -1])
        xlist, ylist = list(xlist), list(ylist)
        xlist.sort()
        ylist.sort()
        modif = sorted(modif, key=lambda x: x[0])
        tree = build_tree(0, len(xlist) - 1)
        pers_trees = [tree]
        new_tree = None
        pref=modif[0][0]
        i=0
        while i<= len(modif) - 1:
            if modif[i][0]!=pref:
                pers_trees.append(new_tree)
                pref = modif[i][0]
            while i!= len(modif) and pref == modif[i][0]:
                new_tree = change_tree(pers_trees[-1] if not new_tree else new_tree,
                                       xlist.index(modif[i][1]), xlist.index(modif[i][2]),
                                       modif[i][3])
                i += 1
        pers_trees.append(tree)
        return pers_trees, xlist, ylist
    return False, False, False

def solver_tree(m,pers_trees, xlist, ylist):
    rec_file = open("точки.txt", "r")
    ans=[]
    if pers_trees is not False:
        for i in range(m):
            x, y = [int(x) for x in rec_file.readline().split()]
            x1 = search(xlist, x)
            y1 = search(ylist, y)
            if x1 == -1 or y1== -1:
                ans.append(0)
            else:
                ans.append(find(pers_trees[y1 + 1], x1))
        return ans
    else:
        for i in range(m):
            ans.append(0)
        return ans


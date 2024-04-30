# алгоритм на карте

def solver_map(m, d, xlist, ylist):
    f = open("точки.txt", "r")
    ans=[]
    for i in range(m):
        x, y = [int(x) for x in f.readline().split()]
        x1 = search(xlist, x)
        y1 = search(ylist, y)
        if x1 == -1 or y1 == -1:
            ans.append(0)
        else:
            ans.append(d[len(ylist)-2-y1][x1])
        return ans  
def prepare_map(n):
    arr = []
    xlist=set()
    ylist=set()
    f= open("прямоугольники.txt", "r")
    for i in range(n):
        p = [int(x) for x in f.readline().split()]
        xlist.add(p[0])
        xlist.add(p[2])
        ylist.add(p[1])
        ylist.add(p[3])
        arr.append(p)
    xlist, ylist = list(xlist), list(ylist)
    xlist.sort()
    ylist.sort()
    d = [[0] * (len(xlist) - 1) for i in range(len(ylist) - 1)]
    for rect in arr:
        compr_x1 = xlist.index(rect[0])
        compr_y1 = ylist.index(rect[1])
        compr_x2 = xlist.index(rect[2])
        compr_y2 = ylist.index(rect[3])
        for x in range(compr_x1, compr_x2):
            for y in range(compr_y1, compr_y2):
                d[len(ylist) - 2 - y][x] += 1
    return d, xlist, ylist

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

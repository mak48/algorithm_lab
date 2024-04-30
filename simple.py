# алгоритм перебора

def enumeration(n, m):
    f = open("прямоугольники.txt", "r")
    rect = [[int(x) for x in f.readline().split()] for i in range(n)]
    f= open("точки.txt", "r")
    ans = []
    for i in range(m):
        x, y = [int(h) for h in f.readline().split()]
        k = 0
        for j in rect:
            if j[0] <= x <j[2] and j[1] <= y < j[3]:
                k+=1
        ans.append(k)
    return ans
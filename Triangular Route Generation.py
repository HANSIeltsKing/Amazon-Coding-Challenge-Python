
# i don't like matrix expression because it is very complicated to show long routes, instead, numbered blocks are more convenient
# eg. 4dim: ([1 2 3 4],[5 6 7 8],[9 10 11 12],[13 14 15 16])
# if you want to generate the number of routes only just search LeetCode 63. Unique Paths II
# it is very stupid to calculate 10dim because it has more than 5000 possible routes (cannot express) so i used 6dim instead
# i will show you a more generalised answer (theoretically available for all dims) to express routes more quickly

def triangle(n):
    l = []
    for i in range(n):
        if i == 0:
            l.append([1])
        elif i == 1:
            l.append([2, 1 + n])
        else:
            y = []
            for j in range(i + 1):
                if j == 0:
                    y.append(i + 1)
                elif j == i:
                    y.append(i * n + 1)
                else:
                    y.append(l[i - 1][j] + 1)
            l.append(y)
    return l


def trianglet(n):
    l = []
    for i in range(n - 1):
        if i == 0:
            l.append([n * n])
        elif i == 1:
            l.append([n * (n - 1), n * n - 1])
        else:
            y = []
            for j in range(i + 1):
                if j == 0:
                    y.append((n - i) * n)
                elif j == i:
                    y.append(n * n - i)
                else:
                    y.append(l[i - 1][j - 1] - 1)
            l.append(y)
    return l

dim = 6
full_triangle = triangle(dim) + list(reversed(trianglet(dim)))
print(full_triangle)

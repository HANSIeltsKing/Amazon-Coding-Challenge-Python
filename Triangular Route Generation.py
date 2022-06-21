
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

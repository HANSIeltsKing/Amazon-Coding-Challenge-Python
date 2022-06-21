
from itertools import product
# if using the random sample of [25, 19, 3, 1, 14, 2, 28, 8, 32, 13] in the case of 6dim
full_triangle = [[1], [2, 7], [3, 8, 13], [4, 9, 14, 19], [5, 10, 15, 20, 25], [6, 11, 16, 21, 26, 31], [12, 17, 22, 27, 32], [18, 23, 28, 33], [24, 29, 34], [30, 35], [36]]
# manually delete all the random samples inside the list a
a = [[1], [7], [3, 8, 13], [4, 9, 14, 19], [5, 10, 15], [6, 11, 16, 21, 31], [12, 22, 27], [18, 28, 33], [24, 34], [], [36]]
add = 1 + int(len(a)/2)
b = []
c = []

tot = list(product(*a))
for j in range(len(tot)):
    if all(tot[j][i] < tot[j][i+1] for i in range(len(tot[j]) - 1)) == True:
        b.append(tot[j])

for j in range(len(b)):
    for i in range(len(b[j]) - 1):
        if b[j][i+1] - b[j][i] > add:
            c.append(b[j])
d = []
for i in range(len(b)):
    if b[i] not in c:
        d.append(b[i])
        
print(d)
print(len(d))
if len(d) == 0:
    print("Unable to reach delivery point")
for i in range(len(a)):
    if a[i] == []:
        print("The " + str(i) + "th layer of the triangle is blocked, which is: " + str(full_triangle[i]))
        
        
        
        

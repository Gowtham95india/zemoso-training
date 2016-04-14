rows = []
with open('_max.txt', 'r') as f:
    for _ in f.readlines():
        rows.append(map(int,_.split()))

for i in range(len(rows)-1, 0, -1):
    for j in range(i):
        rows[i-1][j] += max(rows[i][j],rows[i][j+1])

print rows[0]

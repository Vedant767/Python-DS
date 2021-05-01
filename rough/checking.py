dict = {}
grid = ["GEEKSFORGEEKS",
"GEEKSQUIZGEEK",
"IDEQAPRACTICE"]
a = ['Qui', 'DE', 'Geek']

# print(grid[2][0][0])
for key in a:
    dict[key[0]] = []

a = len(grid)
b = len(grid[0])
# print(a,b)
# print(a[0][0])
list = []
for i in range(a):
    # print(i)
    for j in range(b):
        if grid[i][j] in dict:
            key = grid[i][j]
            list.append([i,j])
            
            # print(key , i,j
            dict[grid[i][j]].append([i,j])
            # print([[i][j]])

for i in dict.values():
    for j,z in i:
        print(j,z)
    # print(i)
# print(dict)
# print(list)

# [[1, 5], [2, 3]]
# [[2, 1]]
# [[0, 0], [0, 8], [1, 0], [1, 9]]
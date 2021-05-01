def check_word(grid, word):
    row = len(grid)
    col = len(grid[0])
    for r in range(row):
        for c in range(col):
            if search(grid, r, c, word, row, col):
                return word,r,c
    return word,-1,-1
        
def search(grid, row, col, word, row_len, col_len):
    if grid[row][col] != word[0]:
        return False
        
    direction = [[-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [0, -1]]    
    for x, y in direction:
        dir1 = row+x
        dir2 = col+y
                
        flag = True
                
        for k in range(1,len(word)):
            if dir1 >= 0 and dir1 < row_len and dir2 >= 0  and dir2 < col_len and word[k] == grid[dir1][dir2]:
                dir1 += x
                dir2 += y
            else:
                flag = False
                break
        if flag:
            return True        
    return False

a = []
grid = []
fetch = []

try:
    while True:
        fetch.append(input().strip())
except:
    print("",end= '')
    
index = fetch.index('')
a = fetch[index+1::]
grid = fetch[:index]
# word, row, col = search_w.check_word(grid, "DAREDEVIL")
# print(f"{word} {row} {col}")
for i in a:
    word, row, col = check_word(grid, i)
    print(f"{word} {row} {col}")
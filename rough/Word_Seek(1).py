class word_search:
    def __init__(self):
        self.row = None
        self.col = None       
    
    def check_word(self, grid, word):
        self.row = len(grid)
        self.col = len(grid[0])
        for row in range(self.row):
            for col in range(self.col):
                if self.search(grid, row, col, word):
                    return word,row,col
        return word,-1,-1
        
    def search(self, grid, row, col, word):
        if grid[row][col] != word[0]:
            return False
        
        direction = [[-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [0, -1]]    
        for x, y in direction:
            dir1 = row+x
            dir2 = col+y
                
            flag = True
                
            for k in range(1,len(word)):
                if dir1 >= 0 and dir1 < self.row and dir2 >= 0  and dir2 < self.col and word[k] == grid[dir1][dir2]:
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
dict = ()
try:
    while True:
        fetch.append(input())
except:
    print("",end= '')
    
index = fetch.index('')
a = fetch[index+1::]
grid = fetch[:index]

search_w = word_search()
# word, row, col = search_w.check_word(grid, "DAREDEVIL")
# print(f"{word} {row} {col}")

for key in a:
    dict[key[0]] = []

for i in a:
    word, row, col = search_w.check_word(grid, i)
    print(f"{word} {row} {col}")
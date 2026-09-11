class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if (r not in range(rows) or 				   #alternative for “r<0 or 
                c not in range(cols) or				   #r==rows or c<0 or or c==cols”
                (r, c) in visit or 
                grid[r][c] == "0"):          			   #return if water or visited
                return

            visit.add((r, c))                 			   #visted, add tuple - {(0,0),(0,1)}
            #cant add list in set/hashmap key
            directions = [[0,1], [0,-1], [1,0], [-1,0]]         #4 possible direction [u,d,l,r]
            for dr, dc in directions:                           #for each direction run dfs
                dfs(r + dr, c + dc)

        #start here
        if not grid or not grid[0]:                             #if empty grid, no islands
            return 0

        res = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])                    #get grid r & c

        for r in range(rows):                                   #go through every row
            for c in range(cols):                               #go through every col
                if grid[r][c] == "1" and (r, c) not in visit:   #water & not visited so +1
                    res += 1                                
                    dfs(r, c)                                  #run dfs for every non-visited comb

        return res

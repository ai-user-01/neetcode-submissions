class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                grid[r][c] == 0
                ):
                return 0
            
            visit.add((r,c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        res = 0

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 1:
                    res = max(res, dfs(r,c))

        return res
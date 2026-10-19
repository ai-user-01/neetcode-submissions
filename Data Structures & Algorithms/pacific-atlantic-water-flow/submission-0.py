class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(r, c, visit, prevHeight):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        rows, cols = len(heights), len(heights[0])
        visitA, visitB = set(), set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for c in range(cols):
            dfs(0, c, visitA, heights[0][c])
            dfs(rows - 1, c, visitB, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, visitA, heights[r][0])
            dfs(r, cols - 1, visitB, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visitA and (r, c) in visitB:
                    res.append([r, c])

        return res

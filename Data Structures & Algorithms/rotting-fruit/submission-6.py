class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def bfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] != 1):
                return False
            grid[r][c] = 2
            q.append((r, c))
            return True

        q = deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        level = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if bfs(r + dr, c + dc):
                        fresh -= 1
            level += 1

        return level if fresh == 0 else -1
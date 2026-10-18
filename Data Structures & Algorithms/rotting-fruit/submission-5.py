class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        res = 0
        count = 0
        q = collections.deque()

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while count > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row in range(rows) and
                        col in range(cols) and
                        grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        count -= 1

            res += 1

        return res if count == 0 else -1

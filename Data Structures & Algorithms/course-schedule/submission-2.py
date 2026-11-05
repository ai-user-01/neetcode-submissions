class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(n1):
            if n1 in visit:
                return False

            if adj[n1] == []:
                return True

            visit.add(n1)
            for n2 in adj[n1]:
                if not dfs(n2):
                    return False
            visit.remove(n1)
            adj[n1] = []
            return True

        visit = set()

        adj = { n1: [] for n1 in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)

        for n1 in range(n):
            if not dfs(n1):
                return False

        return True

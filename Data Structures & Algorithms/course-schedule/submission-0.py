class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:

        adj = {i: [] for i in range(n)}

        for course, prereq in edges:
            adj[course].append(prereq)

        visit = set()

        def dfs(course):
            if course in visit:
                return False

            if not adj[course]:
                return True

            visit.add(course)

            for prereq in adj[course]:
                if not dfs(prereq):
                    return False

            visit.remove(course)
            adj[course] = []
            return True

        for course in range(n):
            if not dfs(course):
                return False

        return True
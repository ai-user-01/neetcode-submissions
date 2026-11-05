class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(n1):					
            if n1 in visit:           			#bc1 - course already visited, loop exists
                return False

            if adj[n1] == []:        			#bc2 - empty list, no prereq
                return True					#these 2 lines can be removed also

            visit.add(n1)             			#add current course to visit
            for n2 in adj[n1]:       			#run dfs on its prereq
                if not dfs(n2):	        		#if it returns false, we return false
                    return False
            visit.remove(n1)          			#remove, prereqs checked so revise preMap
            adj[n1] = []              			#so that next time we can return bc2
            return True                 

        #-----start here					#map each course to: [prereq list]
        visit = set()						#visit = all courses along curr DFS path

        adj = { n1: [] for n1 in range(n) } 			#gives {0: [], 1: [], 2: [], 3: []}
        for n1, n2 in edges:						#gives {0: [1], 1: [2], 2: [3], 3: []} 
            adj[n1].append(n2)				

        for n1 in range(n):
            if not dfs(n1):					#call dfs for every c, bcos our graph can be 
                return False            			#disconnected thats why manually iterate

        return True							#T: O(vertices+edges) = O(n+p)

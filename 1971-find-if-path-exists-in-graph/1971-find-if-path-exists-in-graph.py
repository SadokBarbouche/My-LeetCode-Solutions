class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([source])
        visite = set([source])
        
        while queue:
            noeud = queue.popleft()
            if noeud == destination:
                return True
            for voisin in graph[noeud]:
                if voisin not in visite:
                    visite.add(voisin)
                    queue.append(voisin)
        
        return False
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        
        def euclideanDistance(points):
            return sqrt( points[0] ** 2 + points[1] ** 2 )
        
        distances = []
        for point in points:
            distances.append((euclideanDistance(point) , point))
        
        distances.sort(key=lambda x: x[0])
        
        ans = [i[1] for i in distances]
        
        return ans[:k]
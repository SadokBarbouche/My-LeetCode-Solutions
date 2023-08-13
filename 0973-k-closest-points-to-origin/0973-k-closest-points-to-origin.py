class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        def euclideanDistance(point):
            return point[0] ** 2 + point[1] ** 2
        distances = []
        for point in points:
            heapq.heappush(distances, (euclideanDistance(point), point))
        k_closest = []
        for _ in range(k):
            k_closest.append(heapq.heappop(distances)[1])
        return k_closest
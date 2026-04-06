class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = [-(num) for num in nums]
        heapq.heapify(result)
        for _ in range(k - 1):
            heapq.heappop(result)
            
        return -result[0]

        
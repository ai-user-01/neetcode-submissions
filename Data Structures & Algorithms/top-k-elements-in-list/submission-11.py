class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)                 # key -> value (freq), O(n)
        heap = []                             # min-heap of (value, key), size <= k

        for key, value in count.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)           # drop the least frequent
                
        return [key for _, key in heap]       # O(n log k) time, O(n) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for n in nums:
            nums_dict[n] = 1 + nums_dict.get(n, 0)

        arr = []
        for key, val in nums_dict.items():
            arr.append([val, key])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res

        
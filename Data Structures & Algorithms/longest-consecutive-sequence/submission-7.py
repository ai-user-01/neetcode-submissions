class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # res = 0
        # nums_set = set(nums)
        # for n in nums_set:
        #     streak, curr = 0, n

        #     while curr in nums_set:
        #         streak += 1
        #         curr += 1
            
        #     res = max(res, streak)
        
        # return res

        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                prev = num - 1
                nxt = num + 1
                mp[num] = mp[prev] + mp[nxt] + 1
                mp[num - mp[prev]] = mp[num]
                mp[num + mp[nxt]] = mp[num]
                res = max(res, mp[num])
        return res
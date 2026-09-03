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

        # mp = defaultdict(int)
        # res = 0

        # for num in nums:
        #     if not mp[num]:
        #         mp[num] = mp[num - 1] + mp[num + 1] + 1
        #         mp[num - mp[num - 1]] = mp[num]
        #         mp[num + mp[num + 1]] = mp[num]
        #         res = max(res, mp[num])
        # return res
        nums = set(nums)
        longest = 0

        for num in nums:
            # Only start counting if this is the beginning of a sequence
            if num - 1 not in nums:
                length = 1

                while num + length in nums:
                    length += 1

                longest = max(longest, length)

        return longest
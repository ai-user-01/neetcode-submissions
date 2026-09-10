class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        s_set = set()

        l = 0
        for r in range(len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1

            s_set.add(s[r])
            local_res = len(s_set)
            res = max(res, local_res)

        return res


        
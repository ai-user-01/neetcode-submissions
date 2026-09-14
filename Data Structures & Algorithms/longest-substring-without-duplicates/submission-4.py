class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        s_dict = set()

        for r in range(len(s)):

            while s[r] in s_dict:
                s_dict.remove(s[l])
                l += 1

            s_dict.add(s[r])
            res = max(res, len(s_dict))

        return res
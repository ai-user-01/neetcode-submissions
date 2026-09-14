class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        countf = {}
        maxf = 0
        res = 0

        l = 0
        for r in range(len(s)):
            countf[s[r]] = 1 + countf.get(s[r], 0)
            maxf = max(maxf, countf[s[r]])

            while (r-l+1) - maxf > k:
                countf[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


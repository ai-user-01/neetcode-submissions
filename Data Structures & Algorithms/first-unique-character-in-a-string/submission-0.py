class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}
        for c in s:
            s_dict[c] = 1 + s_dict.get(c, 0)

        # Find first character appearing once
        for i, c in enumerate(s):
            if s_dict[c] == 1:
                return i

        return -1


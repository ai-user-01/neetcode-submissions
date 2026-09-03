class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        s_count = {}
        for s in strs:
            sorted_s = sorted(s)
            sorted_s_str = "".join(sorted_s)
            if sorted_s_str in s_count:
                s_count[sorted_s_str].append(s)
            else:
                s_count[sorted_s_str] = [s]

        return list(s_count.values())

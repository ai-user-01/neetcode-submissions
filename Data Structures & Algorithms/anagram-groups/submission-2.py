class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        s_count = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s)
            sorted_s_str = "".join(sorted_s)
            s_count[sorted_s_str].append(s)
            
        return list(s_count.values())

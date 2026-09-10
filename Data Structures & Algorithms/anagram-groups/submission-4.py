class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        s_dict = defaultdict(list)
        for s in strs:
            sorted_s = str(sorted(s))
            s_dict[sorted_s].append(s)

        return list(s_dict.values())

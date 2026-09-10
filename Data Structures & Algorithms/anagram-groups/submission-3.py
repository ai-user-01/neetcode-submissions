class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []

        s_dict = defaultdict(list)
        for s in strs:
            sorted_s = str(sorted(s))
            s_dict[sorted_s].append(s)

        for k, v in s_dict.items():
            res.append(v)

        return res
            

        

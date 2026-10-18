class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res_dict = defaultdict(list)

        for s in strs:
            sorted_s = str(sorted(s))
            res_dict[sorted_s].append(s)

        return list(res_dict.values())
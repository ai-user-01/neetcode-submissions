class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        s_dict = {}

        for s in strs:
            s_sorted = str(sorted(s))
            if s_sorted in s_dict:
                s_dict[s_sorted].append(s)
            else:
                s_dict[s_sorted] = [s]

        return list(s_dict.values())
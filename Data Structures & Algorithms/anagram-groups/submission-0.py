class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        s_dict = {}
        for s in strs:
            sorted_s_list = sorted(s)
            sorted_s_str = "".join(sorted_s_list)
            if sorted_s_str in s_dict:
                s_dict[sorted_s_str].append(s)
            else:
                s_dict[sorted_s_str] = [s]

        return list(s_dict.values())

        


                
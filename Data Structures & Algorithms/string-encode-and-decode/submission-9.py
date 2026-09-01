class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l

            while s[r] != "#":
                r += 1

            size = int(s[l:r])

            res.append(s[r+1:r+1+size]) #r+1 to skip int num

            l = r + 1 + size

        return res


    # def decode(self, strs: str) -> [str]: 	#Decodes a single string to a list of strings
    #     res = []
    #     i = 0
    #     while i < len(strs):
    #         j = i
    #         while strs[j] not in "0123456789":
    #             j += 1

    #         size = int(strs[j])
    #         res.append(strs[j + 1: j + 1 + size])		
    #         i = j + 1 + size

    #     return res

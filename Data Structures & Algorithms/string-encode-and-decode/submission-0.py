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

            length = int(s[l:r])

            l = r + 1
            r = l + length

            res.append(s[l:r])

            l = r

        return res

    # def encode(self, strs: [str]) -> str:		#Encodes a list of strings to a single string
    #     res = ""
    #     for word in strs:
    #         res += str(len(word)) + word

    #     return res

    # def decode(self, strs: str) -> [str]: 	#Decodes a single string to a list of strings
    #     res = []
    #     i = 0
    #     while i < len(strs):
    #         j = i
    #         while strs[j] not in "0123456789":
    #             j += 1

    #         size = int(strs[j])
    #         res.append(strs[j + 1: j + 1 + size])		#j+1 to skip int num
    #         i = j + 1 + size

    #     return res

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            size = int(s[i:j])

            res.append(s[j+1:j+1+size]) 				#j+1 to skip int num

            i = j + 1 + size						#continue search after word

        return res



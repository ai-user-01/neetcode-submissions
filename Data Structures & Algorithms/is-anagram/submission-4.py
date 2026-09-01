class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):							#cant do for c in s:
            countS[s[i]] = 1 + countS.get(s[i], 0)				#we need to parse each..
            countT[t[i]] = 1 + countT.get(t[i], 0)				#..index of both s & t

        for c in countS:						#combined if statement:
            if c not in countT:					#if countS[c] != countT.get(c, 0):
                return False						#    return False
            if countS[c] != countT[c]:
                return False

        return True

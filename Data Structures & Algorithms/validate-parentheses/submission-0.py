class Solution:
    def isValid(self, s: str) -> bool:
        paramMap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = []
        for c in s:
            if c not in paramMap:
                stack.append(c)
                continue
        
            if not stack:
                return False

            last_param = stack.pop()
            paramMapPair = paramMap[c]

            if last_param != paramMapPair:
                return False

        return not stack
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def helper(l, r):                                     
            while l >= 0 and r < len(s) and s[l] == s[r]:       
                l -= 1							#expand left
                r += 1							#expand right
            return s[l+1:r]		#why s[l+1:r]? suppose odd case & i=0
    #enters with l=0, r=0, 1 len pali found, enters while loop
    #exits with l=-1, r=1, but ret should be s[0:1] or s[l+1:r]

        res = ""								#can write 2 for loops at same level 
        for i in range(len(s)):					#too, 1 for odd, 1 for even
            subRes = helper(i, i)           			#odd len, start from l, r = i, i 
            if len(subRes) > len(res):				#index then expand
                res = subRes

            subRes = helper(i, i+1)         			#even len, start from l, r = i, i+1 
            if len(subRes) > len(res):				#index then expand
                res = subRes

        return res

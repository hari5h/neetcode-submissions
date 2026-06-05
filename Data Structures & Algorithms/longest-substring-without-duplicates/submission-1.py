class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        input
         s = "qweasdzzz"
         lowercase
         ASCII characters
         s = ""
         s = "a"
         s = "xxxx"

         outputs:
         6
         0
         1
         1

         complexity Time space
         loop + hashmap O(n^2) O(n)
         sliding window - O(n) O(n)

         res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res
        """

        l = 0
        res = 0
        charset = set()
        for r in range(len(s)):
            while s[r] in charset and l < r:
                charset.remove(s[l])
                l += 1
            else:
                charset.add(s[r])
            res = max(res, len(charset))
        
        return res
        


        
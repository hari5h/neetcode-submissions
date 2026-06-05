class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#solution 2

        if len(s) != len(t):
            return False

        charCountS = {}
        charCountT = {}

        for i in range(len(s)):
            charCountS[s[i]] = 1 + charCountS.get(s[i], 0)
            charCountT[t[i]] = 1 + charCountT.get(t[i], 0) 

        return charCountS == charCountT




#solution 1
        if len(s) != len(t):
            return False  # Use capital 'F' in False
        return sorted(s) == sorted(t)

# my solution
        charCountMap = {}

        # Count characters in string s
        for char in s:
            if char in charCountMap:
                charCountMap[char] += 1
            else:
                charCountMap[char] = 1  # Fix: was incorrectly using `charCountMap[s]`

        # Subtract character counts based on string t
        for char in t:
            if char in charCountMap:
                charCountMap[char] -= 1
            else:
                return False  # If a char in t isn't in s, they can't be anagrams

        # Check that all values are zero
        return all(count == 0 for count in charCountMap.values())

        
        
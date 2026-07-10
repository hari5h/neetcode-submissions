class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1 = "".join(sorted(s1))
        
        for r in range(len(s2)):
            if r-l+1 > len(s1):
                l += 1

            if r-l+1 == len(s1):
                window = "".join(sorted(s2[l:r+1]))
                if window == s1:
                    return True

        return False
            
        
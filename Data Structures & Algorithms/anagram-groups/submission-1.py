class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}
        for s in strs:
            sortedString = "".join(sorted(s))

            if sortedString not in hashMap:
                hashMap[sortedString] = [s]
            else:
                hashMap[sortedString].append(s)
        
        return list(hashMap.values())


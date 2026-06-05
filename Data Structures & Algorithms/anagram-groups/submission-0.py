class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        
        for string in strs:
            sortedStr = ''.join(sorted(string))
            if sortedStr not in wordDict: 
                wordDict[sortedStr] = [string]
            else:
                wordDict[sortedStr].append(string)

        return wordDict.values()  
        
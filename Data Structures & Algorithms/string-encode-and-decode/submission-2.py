class Solution:

    def encode(self, strs: List[str]) -> str:
        # 4#qqqq

        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string
        print(encodedString)
        return encodedString


    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        while i < len(s):
            stringLength = ""
            while True:
                if s[i] == "#":
                    break
                stringLength +=s[i]
                i += 1
            stringLength = int(stringLength)
            res.append(s[i+1:i+1+stringLength])
            i = i + 1 + stringLength

        return res

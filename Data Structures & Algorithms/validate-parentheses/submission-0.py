class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':"(", "]":"[", "}":"{"}
        stack = []

        for bracket in s:
            if bracket in closeToOpen:
                # handle close bracket
                if len(stack) and stack[-1] == closeToOpen[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                # handle open bracket
                stack.append(bracket)

        return len(stack) == 0
            
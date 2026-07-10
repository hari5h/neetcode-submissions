class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                encoded_string = ""
                while stack[-1] != '[':
                    encoded_string = stack.pop() + encoded_string
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * encoded_string)

        return "".join(stack)

        
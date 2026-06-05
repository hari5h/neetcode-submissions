class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a,b = stack.pop(),stack.pop()
                c = b-a
                stack.append(c)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a,b = stack.pop(),stack.pop()
                c = int(b/a)
                stack.append(c)
            else:
                stack.append(int(token))
        return stack[0]
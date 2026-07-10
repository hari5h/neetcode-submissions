class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] == abs(ast):
                    stack.pop()
                    ast = 0
                elif stack[-1] > abs(ast):
                    ast = 0
                else:
                    stack.pop()

            if ast:
                stack.append(ast)

        return stack
        
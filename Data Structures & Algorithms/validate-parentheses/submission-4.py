class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []

        for c in s:
            if c in ['(', "[", '{']:
                stack.append(c)
            else:
                if c == ')' and len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False

class Solution:
    def is_numeric(self, text):
        try:
            int(text)  # Use float(text) if you need to support decimals
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if self.is_numeric(t):          
                stack.append(int(t))
            else:
                print(stack)
                second_op = stack.pop()
                first_op = stack.pop()
                if t == '+':
                    stack.append(first_op + second_op)
                elif t == '-':
                    stack.append(first_op - second_op)
                elif t == '*':
                    stack.append(first_op * second_op)
                elif t == '/':
                    stack.append(int(first_op / second_op))
        return stack.pop()
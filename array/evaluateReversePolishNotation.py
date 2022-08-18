class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+': lambda a,b: a+b, '*': lambda a,b: a*b, '/': lambda a,b: int(b/a), '-': lambda a,b: b-a}
        for tok in tokens:
            if tok in ops.keys():
                stack.append(ops[tok](stack.pop(),stack.pop()))
            else:
                stack.append(int(tok))
        return stack.pop()
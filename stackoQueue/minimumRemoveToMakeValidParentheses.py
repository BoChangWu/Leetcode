class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        if len(s) == 0:
            return s
        parsedStr = list(s)
        left = []
        right = []
        for idx, val in enumerate(parsedStr):

            if val == '(':
                left.append(idx)
            if val == ')':
           
                if len(left) == 0:
                    right.append(idx)
           
                else:
                    left.pop()

        newList = [value for idx, value in enumerate(parsedStr) if idx not in (left + right)]
        return "".join(newList)
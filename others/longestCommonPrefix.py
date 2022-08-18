class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ['']
        for t in zip(*strs):  # get character of all strings one by one
            c = t[0]   # First Character
            if not all([x==c for x in t]): break  # characters are not same
            res.append(c)
        return ''.join(res)
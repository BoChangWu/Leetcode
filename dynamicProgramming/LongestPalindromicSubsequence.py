class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.get_longest_subseq(0, len(s)-1, s)
    
    def get_longest_subseq(self, start, end, s):

        if start == end:
            return 1
			
        if start > end:
            return 0

        if s[start] == s[end]:
            return 2 + self.get_longest_subseq(start + 1, end - 1, s)
        
        return max(self.get_longest_subseq(start + 1, end, s), self.get_longest_subseq(start, end - 1, s))
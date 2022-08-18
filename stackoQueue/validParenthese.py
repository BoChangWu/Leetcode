class Solution:
    def isValid(self, s: str) -> bool:
        
        while True:
            if "()" in s or "{}" in s or "[]" in s:
                s = s.replace("{}", "")
                s = s.replace("()", "")
                s = s.replace("[]", "")
            elif len(s) != 0:
                return False
            else:
                return True
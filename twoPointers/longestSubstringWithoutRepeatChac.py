def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) < 1:
            return 0
    start = 0 
    end = 1
    count = max_count = 1
    string = s[0]
    while (end < len(s)):
        if(s[end] not in string):
            string+=s[end]
            count+=1
            end+=1
        else:
            max_count = max(count,max_count)
            start+=1
            string = s[start]
            count = 1
            end = start+1
    max_count = max(count,max_count)
    return max_count
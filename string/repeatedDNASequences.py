class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        pt_h = 0
        pt_t= pt_h+9
        sub = set()
        multi_sub=set()
        while pt_t<len(s):
            
            if pt_t==len(s)-1:
                sq = s[pt_h:]
                if  sq in sub:
                    multi_sub.add(sq)
                else:    
                    sub.add(sq)
            else:
                sq = s[pt_h:pt_t+1]
                if sq in sub:
                    multi_sub.add(sq)
                else:    
                    sub.add(sq)
        
            pt_h +=1
            pt_t = pt_h+9
        
        return list(multi_sub)
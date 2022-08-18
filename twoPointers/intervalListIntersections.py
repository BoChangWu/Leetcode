class Solution:
    def intervalIntersection(self, firstlist: List[List[int]], secondlist: List[List[int]]) -> List[List[int]]:
        
        if len(firstlist) ==0 or len(secondlist) ==0:
            return []

        i = 0 
        j = 0
        l = []

        while i < len(firstlist) and j < len(secondlist):

            l.append([max(firstlist[i][0],secondlist[j][0]),min(firstlist[i][1],secondlist[j][1])])

            if l[-1][0]>l[-1][1]:
                l.pop()

            if max(firstlist[i][1],secondlist[j][1]) == firstlist[i][1]:
                j +=1
                continue
            if max(firstlist[i][1],secondlist[j][1]) == secondlist[j][1]:
                i +=1
                continue

            i+=1
            j+=1

        return l
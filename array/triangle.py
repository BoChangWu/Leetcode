class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        out_list = []
        s=0
        def dfs(triangle,row,index,s,out_list):
            
            if row< len(triangle):
                
                if triangle[row][index] !=0:
                    s += triangle[row][index]
                
                dfs(triangle,row+1,index,s,out_list)
                dfs(triangle,row+1,index+1,s,out_list)
            
            else:
                out_list.append(s)
        
        dfs(triangle,0,0,s,out_list)
        
        return min(out_list)
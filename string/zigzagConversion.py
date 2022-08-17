class Solution:
    def convert(self, s: str, numRows: int) -> str:

        z=[]

        def zigzag(s,numRums,z,index,row,dir):
        

            if z==[]:
                for i in range(numRows):
                    z.append([])
            
            if index>= len(s):
                return 

            z[row].append(s[index])
        
            if row ==numRows-1:
                zigzag(s,numRows,z,index+1,row-1,-1)
            elif row ==0:
                zigzag(s,numRows,z,index+1,row+1,1)
            else:
                zigzag(s,numRows,z,index+1,row+dir,dir)
        
        if numRows<2:
            return s
        
        zigzag(s,numRows,z,0,0,1)
        
        ss = ''
        for i in z:
            for k in i:
                ss+= k 

        return ss
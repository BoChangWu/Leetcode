class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_string = []
        for i in num:
            num_string.append(str(i)) # ['1', '2', '0', '0']
            
        num_string = "".join(num_string) # list of chars to single string
        num_string = int(num_string) + k # add and turn to int   
        new_list=[]
        for i in str(num_string):
            new_list.append(int(i))
        return new_list
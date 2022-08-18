class Solution:
    def interpret(self, command: str) -> str:
        
        
        a=command.replace('(al)','al')
        b=a.replace('()','o')
        
        return b
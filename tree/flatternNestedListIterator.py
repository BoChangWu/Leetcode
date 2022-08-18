class NestedIterator:
    def __init__(self, nestedList):
        self.res = []
        def helper(nestedList):
            for x in nestedList:
                if x.isInteger():
                    self.res.append(x.getInteger())
                else:
                    helper(x.getList())
        helper(nestedList)
        self.index = -1
        self.len = len(self.res)
        print(self.res)
    
    def next(self) -> int:
        self.index = self.index + 1
        return self.res[self.index]
        
    
    def hasNext(self) -> bool:
        return self.index < self.len - 1
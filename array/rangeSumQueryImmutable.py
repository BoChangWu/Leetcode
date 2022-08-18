class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        if right+1<len(self.arr):
            return sum(self.arr[left:right+1])
        else:
            return sum(self.arr[left:])
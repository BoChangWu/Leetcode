def sortedSquares(self, nums: List[int]) -> List[int]:
        
    squares = []

    for i in nums:
        squares.append(i*i)

    squares.sort()

    return squares
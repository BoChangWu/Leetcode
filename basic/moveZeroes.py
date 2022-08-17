def move_zeroes(nums:List[int]) ->None:
    zeroes = []
    non_zeroes= []
    for i in range(len(nums)):
        n = nums.pop()
        print(n)
        if n != 0:
            non_zeroes.insert(0,n)
        else:
            zeroes.append(n)
        print(f"non_zero: {non_zeroes},zeroes:{zeroes}")

    nums = non_zeroes + zeroes

    return nums
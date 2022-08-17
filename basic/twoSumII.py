def twoSum(self, numbers: List[int], target: int) -> List[int]:

        indice = []
        for i in range(len(numbers)):
            j = target - numbers[i]
            if j in numbers:
                if numbers.index(j) !=i:
                    indice.append(i+1)
                    indice.append(numbers.index(j)+1)


        indice = list(set(indice))
        indice.sort()
        return indice
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        currentBestScore = values[0] + values[1] - 1
        maxScore = currentBestScore
        
        for i in range(2, len(values)):
            currentBestScore = max(currentBestScore - values[i - 1], values[i - 1]) + values[i] - 1
            maxScore = max(maxScore, currentBestScore)

        return maxScore
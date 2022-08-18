class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        l = len(word)
        stack = []
        boardCharCount = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char == word[0]:
                    stack.append((i, j, 0, set()))
                boardCharCount[char] = boardCharCount.get(char, 0) + 1
                
        wordCharCount = {}
        for char in word:
            wordCharCount[char] = wordCharCount.get(char, 0) + 1
            
        #check if all chars are in board and in sufficient count
        # important for efficient solution
        for (key, value) in wordCharCount.items():
            if key not in boardCharCount:
                return False
            if boardCharCount[key] < wordCharCount[key]:
                return False
        
        
        #dfs
        while stack:
                (x, y, idx, visited) = stack.pop()
                if x < 0 or x > m - 1 or y < 0 or y > n - 1 or  idx > l - 1 or board[x][y] != word[idx] or (x,y) in visited:
                    continue

                if l - 1 == idx:
                    return True

                visited.add((x,y))

                dx = [-1, 0, 1, 0]
                dy = [0, 1, 0, -1]

                for i in range(4):
                    stack.append((x + dx[i], y + dy[i], idx + 1, visited.copy()))
        return False
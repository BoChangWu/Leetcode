class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] + self.ttl > currentTime:
            self.tokens[tokenId] = currentTime 

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for tokenId in self.tokens:
            if self.tokens[tokenId] + self.ttl > currentTime: count += 1
        
        return count
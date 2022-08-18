import heapq
class SeatManager:

    def __init__(self, n: int):
        self.q = [i for i in range(1, n+1)]
        heapq.heapify(self.q)
    def reserve(self) -> int:
        return heapq.heappop(self.q)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.q, seatNumber)
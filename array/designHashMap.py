class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[f'{key}'] = value

    def get(self, key: int) -> int:
        if f'{key}' not in self.map:
            return -1
        return self.map[f'{key}']

    def remove(self, key: int) -> None:
        if f'{key}' in self.map:
            self.map.pop(f'{key}')
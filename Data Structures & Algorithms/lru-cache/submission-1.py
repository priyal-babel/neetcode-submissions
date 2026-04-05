from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = OrderedDict()
        
    def get(self, key: int) -> int:
        if key in self.LRU:
            self.LRU.move_to_end(key)
            return self.LRU[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self.LRU[key] = value
            self.LRU.move_to_end(key)
        else:
            self.LRU[key] = value
            
        if len(self.LRU) > self.capacity:
            self.LRU.popitem(last=False)
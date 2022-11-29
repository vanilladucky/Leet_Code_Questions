class RandomizedSet:

    def __init__(self):
        self.data_map = {} # Keep track of the indexes 
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_map: # O(1)
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map: # O(1)
            return False
        idx_of_val = self.data_map[val]
        last_ele = self.data[-1]
        
        self.data_map[last_ele] = idx_of_val
        self.data_map[val] = len(self.data)-1
        
        self.data[idx_of_val], self.data[-1] = self.data[-1], self.data[idx_of_val]
        
        self.data.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

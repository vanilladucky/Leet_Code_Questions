class TimeMap:

    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_time_map:
            self.key_time_map[key] = {}
        
        self.key_time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_time_map:
            return ""
        
        for curr_time in reversed(range(1, timestamp+1)):
            if curr_time in self.key_time_map[key]:
                return self.key_time_map[key][curr_time]
            
        return ""

# Keep in mind that the timestamps are constantly increasing with the datastream 
class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.keystore:
            values = self.keystore[key]
        else:
            values = []
            
        left, right = 0, len(values)-1
        
        while left<=right:
            mid = (left+right)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
                
        return res

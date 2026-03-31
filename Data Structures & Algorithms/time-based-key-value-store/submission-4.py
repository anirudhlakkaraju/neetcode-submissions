class TimeMap:

    def __init__(self):
        self.mp = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []

        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.mp:
            return res
        vals = self.mp[key]
        n = len(vals)
        lo, hi = 0, n-1

        while lo<=hi:
            mid = lo + (hi-lo)//2

            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                lo = mid+1
            else:
                hi = mid-1

        return res
        

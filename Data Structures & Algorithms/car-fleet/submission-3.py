class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        a = []
        for i in range(n):
            a.append((position[i], speed[i]))
        
        # Sort by position
        a.sort()

        # Compute time taken each car
        t = []
        for i in range(n):
            time = (target-a[i][0])/a[i][1]
            t.append(time)
        
        res = []
        for i in range(n-1, -1, -1):
            if not res or res[-1] < t[i]:
                res.append(t[i]) 
        
        return len(res)

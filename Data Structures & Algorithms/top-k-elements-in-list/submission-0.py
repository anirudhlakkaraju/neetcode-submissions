class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}

        for num in nums:
            if num not in m:
                m[num] = 0
            m[num] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for key, values in m.items():
            buckets[values].append(key)
        
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for val in buckets[i]:
                if len(res) == k:
                    return res
                res.append(val)
        
        return res
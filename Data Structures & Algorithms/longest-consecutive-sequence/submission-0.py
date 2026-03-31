class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            m[num] = 1
        
        res = 0
        for num in nums:
            if num-1 not in m:
                i = num
                seq = 0
                while i in m:
                    seq += 1
                    i += 1
                
                res = max(res, seq)
    
        return res

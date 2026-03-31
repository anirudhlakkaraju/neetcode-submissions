class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) * len(matrix[0]) - 1

        while lo < hi:
            mid = lo + (hi-lo)//2

            r, c = mid//len(matrix[0]), mid%(len(matrix[0]))

            if matrix[r][c] >= target:
                hi = mid
            else:
                lo = mid + 1
            
        
        r, c = hi//len(matrix[0]), hi%(len(matrix[0]))
        if matrix[r][c] == target:
            return True
        
        return False
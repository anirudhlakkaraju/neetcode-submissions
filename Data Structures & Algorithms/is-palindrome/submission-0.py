class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for c in s:
            if c != ' ' and c.isalnum():
                t += c.lower()
        
        left = 0
        right = len(t)-1

        while left <= right:
            if t[left] != t[right]:
                return False
            left += 1
            right -= 1
        
        return True

        
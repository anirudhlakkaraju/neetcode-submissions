class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1

            if tuple(count) not in m:
                m[tuple(count)] = []
                
            m[tuple(count)].append(word)
        
        return list(m.values())

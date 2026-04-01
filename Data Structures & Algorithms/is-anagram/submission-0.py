from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        freq = defaultdict(int)
        for letter in s:
            freq[letter] += 1
        for letter in t:
            freq[letter] -= 1
        for val in freq.values():
            if val != 0: return False
        return True

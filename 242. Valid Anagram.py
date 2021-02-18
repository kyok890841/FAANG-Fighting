class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted([ord(c) for c in s]) == sorted([ord(c) for c in t]) else False

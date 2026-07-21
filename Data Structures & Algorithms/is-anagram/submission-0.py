class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_s = ''.join(sorted(s))
        string_t = ''.join(sorted(t))
        if string_s == string_t:
            return True
        return False
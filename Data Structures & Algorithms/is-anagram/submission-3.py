class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        s = sorted(s)
        t = sorted(t)
        for i in range(max(s_len, t_len)):
            if i >= s_len or i >= t_len:
                return False
            if s[i] != t[i]:
                return False

        return True
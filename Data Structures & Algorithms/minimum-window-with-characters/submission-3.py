from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        if s == t: return s
        t_count = Counter(t)
        s_count = {}
        res = ""
        l = 0

        for r in range(len(s)):
            if s[r] in t_count:
                s_count[s[r]] = s_count.get(s[r], 0) + 1
            print(s[r], l, r, s_count, t_count)
            print(all(k in s_count for k, v in t_count.items()))
            while all(v <= s_count.get(k,0) for k, v in t_count.items()):
            # while s_count == t_count:
                if res == '':
                    res = s[l:r + 1]
                elif len(res) > (r - l + 1):
                    res = s[l:r + 1] 
                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    # if s_count[s[l]] == 0:
                    #     del s_count[s[l]]
                l += 1
                print(res)           
            
            
            
        
        return res
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for c1, c2 in zip(s, t):
            count[c1] = count.get(c1, 0) + 1
            count[c2] = count.get(c2, 0) - 1
         
        return all((v == 0 for v in count.values()))
        # if len(s) != len(t):
        #     return False
        # s_count, t_count = {}, {}
        
        # for char in s:
        #     if char not in s_count:
        #         s_count[char] = 1
        #     else:
        #         s_count[char] += 1
        
        # for char in t:
        #     if char not in t_count:
        #         t_count[char] = 1
        #     else:
        #         t_count[char] += 1

        # return s_count == t_count
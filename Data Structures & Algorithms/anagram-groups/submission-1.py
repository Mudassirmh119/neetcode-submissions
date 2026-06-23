from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            li = [0] * 26
            for c in s:
                asci = ord(c) - 97
                li[asci] = li[asci] + 1
            
            groups[tuple(li)].append(s)
        return list(groups.values())

        # for s in strs:
        #    _s = "".join(sorted(s))
        #    if _s not in groups:
              
        #       groups[_s] = [s]
        #    else:
        #       groups[_s].append(s)
        # return list(groups.values())
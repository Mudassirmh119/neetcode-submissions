class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
           _s = "".join(sorted(s))
           if _s not in groups:
              groups[_s] = [s]
           else:
              groups[_s].append(s)
        return list(groups.values())
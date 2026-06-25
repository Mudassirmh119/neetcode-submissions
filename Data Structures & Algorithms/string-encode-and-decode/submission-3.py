class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += f"{len(s)}#{s}"                    
        print('result', result)
        return result
            
    def decode(self, s: str) -> List[str]:
        li = []
        i = 0;
        while i < len(s):            
            j = i
            while s[j] != '#':
                j += 1
            
            _len = int(s[i:j])
            li.append(s[j + 1: j + _len + 1])            
            i = j + _len + 1
        return li
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += f"###"
            for c in s:
                result += chr(ord(c) + 1)
                print('convert', c, chr(ord(c) + 1))
        
        return result
            
    def decode(self, s: str) -> List[str]:
        _strs = re.split(r'###', s)
        print("_strs", _strs)
        _strs.pop(0)
        
        strs = []

        for _str in _strs:    
            if len(_str) == 0:
                strs.append("")
            else:
                s_item = ''
                for c in _str:
                    s_item += chr(ord(c) - 1)
                strs.append(s_item)
        
        
        # for i in range(len(s)):
        #     print('i', i)
        #     if s[i] == '#' and i + 1 < len(s) and s[i + 1].isdigit():
        #         print("check chr",s[i + 1] ,s[i + 1].isdigit())
        #         s_item = ''
        #         for j in range(int(s[i + 1])):
        #             print('ij', i, j)
        #             if i + 2 < len(s):
        #                 s_item += chr(ord(s[i + 2]) - 1)
        #                 i += 1
        #         print('s_item', s_item)
        #         strs.append(s_item)
        # print('strs', strs) 
        return strs

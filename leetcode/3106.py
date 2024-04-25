from itertools import pairwise

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        out = ""
        a = ord('a')
        z = ord('z')
        for index, char in enumerate(s):
            o = ord(char)
            dis = min(o-a,z-o+1)
            if dis>k:
                out = out+chr(o-k)+s[index+1:]
                break
            elif dis == 0:
                out += char
            else:
                out += 'a'
                k -= dis
        return out


Solution().getSmallestString("zbbz",3)
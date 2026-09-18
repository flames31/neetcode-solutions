class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            i = j + 1
            strs.append(s[i:i + length])
            i += length
        
        return strs
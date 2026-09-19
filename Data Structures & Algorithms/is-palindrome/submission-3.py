class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = ''.join(s.split()).lower()
        l, r = 0, len(v)-1
        while l < r:
            if not v[l].isalnum():
                l += 1
                continue
            if not v[r].isalnum():
                r -= 1
                continue
            if v[l] != v[r]:
                return False
            l += 1
            r -= 1
        
        return True
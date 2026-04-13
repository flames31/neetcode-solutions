class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		se = set()
		ans = 0

		i, j = 0, 0

		while j < len(s):
			if s[j] not in se:
				se.add(s[j])
				ans = max(ans, j-i+1)
				j += 1
			else:
				while i < j and s[j] in se:
					se.remove(s[i])
					i += 1
		
		return ans
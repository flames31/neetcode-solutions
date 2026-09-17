class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        ans = nums[:]
        for num in nums:
            ans.append(num)
        
        return ans
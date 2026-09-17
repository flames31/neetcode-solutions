class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first, second = 0, 0
        while second < len(nums):
            if nums[second] != val:
                nums[first] = nums[second]
                first += 1
            second += 1
        
        return first
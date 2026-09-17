class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 1
        major_ele = nums[0]
        for num in nums:
            if num == major_ele:
                count += 1
            else:
                count -= 1
                if count == 0:
                    major_ele = num
                    count = 1
        
        return major_ele
                
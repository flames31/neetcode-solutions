class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]

        for idx in range(1, len(nums)):
            result[idx] = nums[idx-1] * result[idx-1]

        prod = nums[-1]

        for idx in range(len(nums)-2, -1, -1):
            result[idx] *= prod
            prod *= nums[idx]
        
        return result
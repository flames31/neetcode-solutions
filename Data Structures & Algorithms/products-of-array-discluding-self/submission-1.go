func productExceptSelf(nums []int) []int {
    result := make([]int, len(nums))
    result[0] = 1

    for i:=1;i<len(nums);i++ {
        result[i] = result[i-1] * nums[i-1]
    }

    prod := nums[len(nums)-1]
    for i:=len(nums)-2;i>=0;i-- {
        result[i] *= prod
        prod *= nums[i]
    }

    return result
}

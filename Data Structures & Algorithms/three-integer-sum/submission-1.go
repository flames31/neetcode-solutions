func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	ans := make([][]int, 0)

	for i:=0; i <len(nums)-2;i++ {
		if i > 0 && nums[i] == nums[i-1] { continue }

		j, k := i+1, len(nums)-1

		for j < k {
			if nums[i] + nums[j] + nums[k] == 0 {
				ans = append(ans, []int{nums[i], nums[j], nums[k]})
				j++
				k--

				for j < k && nums[j] == nums[j-1] { j++ }
				for j < k && nums[k] == nums[k+1] { k-- }
			} else if nums[i] + nums[j] + nums[k] > 0 {
				k--
			} else {
				j++
			}
		}
	}

	return ans
}

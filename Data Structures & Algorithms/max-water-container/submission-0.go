func maxArea(heights []int) int {
	i, j := 0, len(heights)-1
	maxWater := 0

	for i < j {
		water := (j-i) * min(heights[i], heights[j])
		maxWater = max(maxWater, water)

		if heights[i] > heights[j] { 
			j-- 
		} else { 
			i++ 
		}
	}

	return maxWater
}

func max(a, b int) int {
	if a > b { return a }
	return b
}

func min(a,b int) int {
	if a < b { return a }
	return b
}

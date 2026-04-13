func maxProfit(prices []int) int {
	mProf := 0
	least := math.MaxInt

	for _, p := range prices {
		if p < least {
			least = p
		}

		if p - least > mProf {
			mProf = p - least
		}
	}

	return mProf
}

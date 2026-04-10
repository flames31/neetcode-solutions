func topKFrequent(nums []int, k int) []int {
    l := make([][]int, len(nums)+1)
    counts := make(map[int]int)

    for _, num := range nums {
        counts[num]++
    }

    for k, v := range counts {
        l[v] = append(l[v], k)
    }

    ans := make([]int, 0)

    for i := len(nums); i >= 0 ; i-- {
        if len(l[i]) > 0 {
            for _, e := range l[i] {
                ans = append(ans, e)
                if len(ans) == k {
                    return ans
                }
            }
        }
    }

    return ans
}
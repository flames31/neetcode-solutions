func isPalindrome(s string) bool {
	i, j := 0, len(s) - 1
	
	s = strings.ToLower(s)
	for i < j {
		if !allowed(rune(s[i])) { 
			i++
			continue
		}
		if !allowed(rune(s[j])) { 
			j-- 
			continue
		}
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}

	return true
}

func allowed(r rune) bool {
	if ('a' <= r  && r <= 'z') || ('0' <= r && r <= '9') {
		return true
	}

	return false
}
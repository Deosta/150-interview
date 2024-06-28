// With Go, the process was a bit different, due to how the language operates. Obviously, import anything needed in main().

// 1. Set passed string = to itself and use the ToLower() method for all lowercase
// 2. Create a new string to hold the modified passed string
// 3. Since there isn't really a build in function for the language that parses strings for alphanumeric, we need to import regexp and use MustCompile and MatchString to check for alphanumeric.
// 3. Loop through the string, if the char at the index IsLetter, append to new string
// 4. Set Two Pointers one pointed at the beginning of the string, the other at the end
// 5. step the pointers, comparing left and right to each other, if not equal to each other return False, increment the left side, decrement the right, otherwise return True

func isPalindrome(s string) bool {

	s = strings.ToLower(s)
	new_string := ""
	IsLetter := regexp.MustCompile(`^[a-zA-Z0-9]+$`).MatchString

	for i := range len(s) {
		if IsLetter(string(s[i])) {
			new_string += string(s[i])
		}
	}

	left := 0
	right := len(new_string) - 1
	for left <= right {
		if new_string[left] != new_string[right] {
			return false
		}
		left += 1
		right -= 1
	}
	return true
}
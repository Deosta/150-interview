# This one tripped me up in college and it tripped me up here too. I had forgotten about the Two Pointer and was trying to work with one string and replace anything non-alphanumeric with "". This was clunky and honestly didn't work. I reviewed various solutions. I tend to stay away from the 2 line solutions as those do not explain why I was wrong. The solution that resonated with me had the following algorithm/logic:

# 1. Create an empty string to hold the newly formed string
# 2. Step through the string, make everything lowercase
# 3. Using Python, check for alphanumeric, if True, append to the new string
# 4. Set Two Pointers one pointed at the beginning of the string, the other at the end
# 5. step the pointers, comparing left and right to each other, if not equal to each other return False, increment the left side, decrement the right, otherwise return True

class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_string = ""
        for char in s:
            if char.isalnum():
                new_string += char.lower()
        
        left, right = 0, len(new_string) - 1

        while left <= right:
            if new_string[left] != new_string[right]:
                return False
            left += 1
            right -= 1
        return True
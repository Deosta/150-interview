// C# didn't change very much from Python. Thankfully, it's robust enough to have an included function that checks for IsLetterOrDigit.

// 1. Set passed string = to itself and use the ToLower() method for all lowercase
// 2. Create a new string to hold the modified passed string
// 3. Loop through the string, if the char IsLetterOrDigit, append to new string
// 4. Set Two Pointers one pointed at the beginning of the string, the other at the end
// 5. step the pointers, comparing left and right to each other, if not equal to each other return False, increment the left side, decrement the right, otherwise return True

public class Solution {
    public bool IsPalindrome(string s) {
        s = s.ToLower();
        string new_string = "";
        for(int i = 0; i < s.Length; i++) {
            if (Char.IsLetterOrDigit(s[i])) {
                new_string += s[i];
            }
        }

        int left = 0;
        int right = new_string.Length - 1;
        while(left <= right) {
            if(new_string[left] != new_string[right]) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
}
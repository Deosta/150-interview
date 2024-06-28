// JS was very similar to Go. It doesn’t seem to have a method that checks for alphanumeric. I used regexp again. A good tool for the toolbox, so to speak.

// 1. Set passed string = to itself and use the toLowerCase() method for all lowercase
// 2. Create a new string to hold the modified passed string
// 3. Since there isn't really a build in function for the language that parses strings for alphanumeric, we need to use regex to check for alphanumeric.
// 3. Loop through the string, if the char at the index IsLetter, append to new string
// 4. Set Two Pointers one pointed at the beginning of the string, the other at the end
// 5. step the pointers, comparing left and right to each other, if not equal to each other return False, increment the left side, decrement the right, otherwise return True

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.toLowerCase()
    regexp = /^[A-Za-z0-9]+$/;
    //console.log(s)
    let new_string = ""
    for(let i = 0; i < s.length; i++) {
        if (regexp.test(s[i])) {
            new_string += s[i]
        }
    }

    let left = 0
    let right = new_string.length - 1
    while(left <= right) {
        if(new_string[left] != new_string[right]) {
            return false
        }
        left += 1
        right -= 1
    }
    return true
};
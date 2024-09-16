class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #utilize python to split the string storing it in a list variable called words
        words = s.split()
        #Get the length of the last word in the words list and store it in last_word_length variable
        last_word_length = len(words[-1])
        return last_word_length
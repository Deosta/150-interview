# 1. Take the given array and convert to a string
# 2. Convert new string to an int
# 3. Add one to the int
# 4. Convert to string, add to array, converting each index to int
# 5. Return the new array
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #take the array and turn it into a string
        temp_num = int(''.join(str(i) for i in digits))
        #add one to the number
        res = list(str(temp_num+1))
        #return an array of new int
        res = list(map(int,res))
        return res
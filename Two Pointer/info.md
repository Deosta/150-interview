Two pointer approach is an essential part of a programmer’s toolkit, especially in technical interviews. The name does justice in this case, it involves using two pointers to save time and space. (Here, pointers are basically array indexes).
Just like Binary Search is an optimization on the number of trials needed to achieve the result, this approach is used for the same benefit.

The idea here is to iterate two different parts of the array simultaneously to get the answer faster. General implimentation is as follows:

```
def doSomething(self, nums):

    left, right = 0, len(nums) - 1

            while left <= right:
                if nums[left] != nums[right]:
                    return False
                left += 1
                right -= 1
            return True
```

As you can see, we are creating a left and a right pointer variable. One is set to the left side of the list, the other to the right. The important bit is while the left side is less than or equal to the right, we do work. We increment left by one and decrement right by one until we meet in the middle of the list.
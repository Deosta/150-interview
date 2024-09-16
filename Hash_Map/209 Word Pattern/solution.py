class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #split the list of words and store it in listOfStrings
        listOfStrings = s.split(' ')
        list1 = []
        list2 = []

        #loop through pattern and through listOfStrings store the index 
        for i in pattern:
            list1.append(pattern.index(i))
        print(list1)
        for i in listOfStrings:
            list2.append(listOfStrings.index(i))
        print(list2)

        #compare the lists, if the indexes match, return True
        if list1 == list2:
            return True
        else:
            return False
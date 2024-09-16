class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #create two lists to store
        map1 = []
        map2 = []
        for i in s:
            map1.append(s.index(i))
        print(map1)
        for i in t:
            map2.append(t.index(i))
        print(map2)
        if map1 == map2:
            return True
        return False
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # let's create a map for a counter and list of the str for the first one 
        # for the second check if counter was in the map if yes just add the str to list at that counter else create another one with it's counter and list with it 
        # finally go through the map and return only the lists stored
        f={}
        for s in strs:
            c=frozenset(Counter(s).items())
            if c in f:
                f[c].append(s)
            else:
                f[c]=[s]
        ans=[x for i,x in f.items()]
        return ans
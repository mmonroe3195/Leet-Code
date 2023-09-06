from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        counters = []
        dict = {}
        # loop through each word in the list and create a counter for each word
        # this counter will be used to keep track of anagrams
        for word in strs:
            counter = Counter()
            for j in word:
                counter[str(j)] += 1
            
            # use each counter as a key for a dictionary
            # each word with the same counter is an anagram so the word should be appended as a value for the key
            
            key = tuple(sorted(counter.items()))
            if dict.get(key):
                dict[key].append(str(word))
            else:
                dict[key] = [str(word)]
                
        return dict.values()
            

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    w1 = {}
    for i in s:
        if w1.get(i) is None:
            w1[i] = 1
        else:
            w1[i] += 1
            
    for i in t:
        if w1.get(i) is None:
            return False
        else:
            w1[i] -= 1
    
    for i in w1:
        if w1[i] != 0:
            return False
        
    return True
    
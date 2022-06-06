from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    groups = {}
    
    for v in strs:
        rep = "".join(sorted(v))
        if groups.get(rep) is not None:
            groups[rep].append(v)
        else:
            groups[rep] = [v]
    
    return list(groups.values())

def groupAnagramsHashmap(strs):
    res = defaultdict(list)

    for i in strs:
        count = [0] * 26
        for l in i:
            count[ord(l)-ord("a")] += 1
        
        res[tuple(count)].append(i)


    return list(res.values())

out = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(out)
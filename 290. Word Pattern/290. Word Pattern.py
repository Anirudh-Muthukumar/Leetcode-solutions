import collections

class Solution:
    def wordPattern(self, pattern, str):
        mp = collections.defaultdict()
        words = str.split()
        n = len(words)
        if n!=len(pattern):
            return False
        
        for i in range(n):
            if pattern[i] not in mp:
                if words[i] not in mp.values():
                    mp[pattern[i]] = words[i]
                else:
                    return False
            elif mp[pattern[i]] != words[i]:
                return False
        
        return True
        
        
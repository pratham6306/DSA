class Solution(object):
    def numberOfSubstrings(self, s):
        freq = {'a' : 0, 'b' : 0, 'c' : 0}  
        ans = 0
        i = 0
        n = len(s)
        for j in range(n):
            freq[s[j]] += 1
            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                ans += n - j
                freq[s[i]] -= 1
                i += 1
        return ans
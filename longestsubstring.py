class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        temp = 0
        substring = ''
        n = len(s)
        for i in range(n):
            if substring.count(s[i]) == 0:
                substring += s[i]
                temp += 1
                ans = max(ans, temp)
            elif substring.count(s[i]) == 1:
                substring += s[i]
                substring = substring[substring.index(s[i])+1:]
                temp = len(substring)
        return ans 

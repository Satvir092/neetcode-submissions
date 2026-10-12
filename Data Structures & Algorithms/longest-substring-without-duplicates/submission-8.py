class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict

        dup = defaultdict(int)

        maxi = 0

        l = 0
        r = 0

        output = 0

        while r < len(s):

            if dup[s[r]] > 0:

                while l < r and dup[s[r]] > 0:

                    dup[s[l]] -= 1
                    output -= 1
                    l += 1
            
            output += 1
            dup[s[r]] += 1
            
            maxi = max(maxi, output)

            r += 1

        return maxi


 

        
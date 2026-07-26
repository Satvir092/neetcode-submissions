class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        ltr = defaultdict(int)
        top = 0

        while r < len(s):

            ltr[s[r]] += 1

            while (r - l + 1) - max(ltr.values()) > k:

                ltr[s[l]] -= 1

                l += 1

            top = max(top, r - l + 1)

            r += 1

        return top



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        letters = set()
        best = 0

        while r < len(s):

            if s[r] not in letters:

                letters.add(s[r])

            else:

                while s[r] in letters:

                    print(s[r], letters)

                    letters.discard(s[l])
                    l += 1

                letters.add(s[r])

            best = max(best, r - l + 1)

            r += 1

        return best
        
class Solution:
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:

        let = defaultdict(int)

        cur = defaultdict(int)

        for letter in s1:

            cur[letter] += 1

        l = 0
        r = 1

        while r <= len(s2):

            string = s2[l:r]

            if len(string) == len(s1):

                for letter in string:

                    let[letter] += 1

                if let == cur:

                    return True

                else:

                    let = defaultdict(int)
                    l += 1

            r += 1

        return False




        
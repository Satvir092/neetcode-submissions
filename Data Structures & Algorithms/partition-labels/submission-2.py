class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import defaultdict

        counts = defaultdict(int)

        for letter in s:

            counts[letter] += 1

        output = []

        r = 0

        c_string = ""

        bum = False

        while r < len(s):

            c_string += s[r]

            counts[s[r]] -= 1

            for letter in c_string:

                if counts[letter] != 0:
                    bum = True

            if not bum:

                output.append(len(c_string))
                c_string = ""
            bum = False
            r += 1

        return output



        
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        cur_str = ""
        sub = ""

        while a or b or c:

            if sub == "aa":
                
                maxi = max(b, c)

            elif sub == "bb":

                maxi = max(a, c)

            elif sub == "cc":

                maxi = max(a, b)

            else:

                maxi = max(a, b, c)

            if maxi == a and sub != "aa" and a > 0:

                cur_str += "a"
                if sub and sub[-1] != "a":

                    sub = ""

                else:

                    sub += "a"

                a -= 1

            elif maxi == b and sub != "bb" and b > 0:

                cur_str += "b"
                if sub and sub[-1] != "b":

                    sub = ""

                else:

                    sub += "b"

                b -= 1

            elif maxi == c and sub != "cc" and c > 0:

                cur_str += "c"
                if sub and sub[-1] != "c":

                    sub = ""

                else:

                    sub += "c"

                c -= 1

            else:

                break

        return cur_str

            


        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        from collections import deque

        numbers = deque()

        output = 0

        for token in tokens:

            if token == "+" or token == "*" or token == "-" or token == "/":

                b = int(numbers.pop())
                a = int(numbers.pop())

                if token == "+":
                    output = a + b

                if token == "-":
                    output = a - b

                if token == "/":
                    output = int(a / b)

                if token == "*":
                    output = a * b

                numbers.append(output)

            else:

                numbers.append(int(token))

        return numbers.pop()

        
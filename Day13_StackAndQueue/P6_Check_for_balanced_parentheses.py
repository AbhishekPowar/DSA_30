# Check_for_balanced_parentheses

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        match = {'{': '}', '[': ']', '(': ')'}
        for ch in s:
            if len(stack) > 0:
                last = stack[-1]
                if match.get(last, None) == ch:
                    stack.pop()
                else:
                    stack.append(ch)

            else:
                stack.append(ch)

        print(''.join(stack))
        return len(stack) == 0


if __name__ == "__main__":
    s = '{{}}()'
    out = Solution().isValid(s)
    print('isValid = ', out)

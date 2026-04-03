class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif not stack or stack[-1] != matches[c]:
                return False
            else:
                stack.pop()
        return not stack


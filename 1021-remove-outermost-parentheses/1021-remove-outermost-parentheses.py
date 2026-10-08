class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        open = 0
        res = []

        for ch in s:
            if ch == '(':
                if open > 0:
                    res.append(ch)
                open += 1
            else:
                open -= 1
                if open > 0:
                    res.append(ch)

        return ''.join(res)
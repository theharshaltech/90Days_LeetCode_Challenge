class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    sub, i = parse(i + 1)
                    current = {a + b for a in current for b in sub}

                elif expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                else:
                    current = {a + expression[i] for a in current}
                    i += 1

            result |= current

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)
        return sorted(result)
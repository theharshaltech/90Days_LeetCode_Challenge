class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        cnt = Counter(s)

        odd = [c for c in cnt if cnt[c] % 2]
        if len(odd) > 1:
            return ""

        half_len = n // 2
        half_cnt = Counter()

        for c in cnt:
            half_cnt[c] = cnt[c] // 2

        mid = odd[0] if odd else ""

        def palindrome(left):
            left = ''.join(left)
            return left + mid + left[::-1]

        # Try the half equal to target's first half
        used = Counter()
        possible = True

        for i in range(half_len):
            c = target[i]
            used[c] += 1

            if used[c] > half_cnt[c]:
                possible = False
                break

        if possible:
            left = list(target[:half_len])
            candidate = palindrome(left)

            if candidate > target:
                return candidate

        # Find the next lexicographically larger half
        for i in range(half_len - 1, -1, -1):
            used = Counter(target[:i])

            if any(used[c] > half_cnt[c] for c in used):
                continue

            for c in sorted(half_cnt):
                if c <= target[i]:
                    continue

                if used[c] >= half_cnt[c]:
                    continue

                new_half = list(target[:i])
                new_half.append(c)

                remaining = half_cnt.copy()

                for x in new_half:
                    remaining[x] -= 1

                for x in sorted(remaining):
                    new_half.extend([x] * remaining[x])

                candidate = palindrome(new_half)

                if candidate > target:
                    return candidate

        return ""
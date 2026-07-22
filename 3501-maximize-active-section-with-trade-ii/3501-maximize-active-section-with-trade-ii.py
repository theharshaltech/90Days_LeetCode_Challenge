class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        total_ones = s.count('1')

        zero_groups = []
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                zero_groups.append((i, j - 1))
                i = j
            else:
                i += 1

        num_zg = len(zero_groups)

        full_gains = []
        for k in range(num_zg - 1):
            len_k = zero_groups[k][1] - zero_groups[k][0] + 1
            len_k1 = zero_groups[k+1][1] - zero_groups[k+1][0] + 1
            full_gains.append(len_k + len_k1)

        m = len(full_gains)
        st = []
        if m > 0:
            LOG = m.bit_length()
            st = [[0] * m for _ in range(LOG)]
            st[0] = list(full_gains)
            for j in range(1, LOG):
                length = 1 << (j - 1)
                for k in range(m - (1 << j) + 1):
                    st[j][k] = max(st[j - 1][k], st[j - 1][k + length])

        def query_rmq(L, R):
            if L > R or m == 0:
                return 0
            length = R - L + 1
            j = length.bit_length() - 1
            return max(st[j][L], st[j][R - (1 << j) + 1])

        zg_starts = [g[0] for g in zero_groups]
        zg_ends = [g[1] for g in zero_groups]

        def get_eff_len(idx, l, r):
            st_i, en_i = zero_groups[idx]
            eff_st = max(st_i, l)
            eff_en = min(en_i, r)
            return max(0, eff_en - eff_st + 1)

        ans = []

        for l, r in queries:
            max_gain = 0

            idx_start = bisect.bisect_left(zg_ends, l)
            idx_end = bisect.bisect_right(zg_starts, r) - 1

            if idx_start < idx_end:
                if zero_groups[idx_start][1] >= l and zero_groups[idx_start + 1][0] <= r:
                    g_first = get_eff_len(idx_start, l, r) + get_eff_len(idx_start + 1, l, r)
                    max_gain = max(max_gain, g_first)

                if zero_groups[idx_end - 1][1] >= l and zero_groups[idx_end][0] <= r:
                    g_last = get_eff_len(idx_end - 1, l, r) + get_eff_len(idx_end, l, r)
                    max_gain = max(max_gain, g_last)

                first_full_k = bisect.bisect_left(zg_starts, l)
                last_full_k1 = bisect.bisect_right(zg_ends, r) - 1
                last_full_k = last_full_k1 - 1

                if first_full_k <= last_full_k:
                    max_gain = max(max_gain, query_rmq(first_full_k, last_full_k))

            ans.append(total_ones + max_gain)

        return ans
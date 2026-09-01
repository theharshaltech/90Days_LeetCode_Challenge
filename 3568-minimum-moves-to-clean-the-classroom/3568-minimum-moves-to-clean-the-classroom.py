class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = {}

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        total_litter = len(litter)

        if total_litter == 0:
            return 0

        full_mask = (1 << total_litter) - 1

        best = [
            [[-1] * (1 << total_litter) for _ in range(n)]
            for _ in range(m)
        ]

        sr, sc = start

        q = deque()

        best[sr][sc][0] = energy
        q.append((sr, sc, 0, energy, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            r, c, mask, curr_energy, moves = q.popleft()

            if mask == full_mask:
                return moves

            if curr_energy == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = curr_energy - 1

                new_mask = mask

                if classroom[nr][nc] == 'L':
                    bit = litter[(nr, nc)]
                    new_mask |= (1 << bit)

                if classroom[nr][nc] == 'R':
                    new_energy = energy

                if best[nr][nc][new_mask] >= new_energy:
                    continue

                best[nr][nc][new_mask] = new_energy

                q.append((
                    nr,
                    nc,
                    new_mask,
                    new_energy,
                    moves + 1
                ))

        return -1
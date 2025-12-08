import sys


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    results = []

    for _ in range(t):
        n = int(data[idx]);
        idx += 1
        p = [int(x) - 1 for x in data[idx:idx + n]];
        idx += n

        visited = [False] * n
        color = [''] * n

        for i in range(n):
            if not visited[i]:

                cycle = []
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    cycle.append(curr)
                    curr = p[curr]

                if len(cycle) % 2 == 0:
                    for j, node in enumerate(cycle):
                        color[node] = 'R' if j % 2 == 0 else 'G'
                else:
                    for j in range(len(cycle) - 1):
                        node = cycle[j]
                        color[node] = 'R' if j % 2 == 0 else 'G'
                    color[cycle[-1]] = 'B'

        results.append(''.join(color))

    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
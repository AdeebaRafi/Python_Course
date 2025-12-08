def busy_beaver_arrangement(test_cases):
    results = []
    for X, Y, Z in test_cases:
        total = X + Y + Z
        counts = {'M': X, 'I': Y, 'T': Z}

        if max(counts.values()) > (total + 1) // 2:
            results.append(('NO', None))
            continue

        arrangement = []
        for _ in range(total):
            candidates = []
            for c in 'MIT':
                if counts[c] == 0:
                    continue
                if arrangement and arrangement[-1] == c:
                    continue
                if len(arrangement) >= 2:
                    last_two = arrangement[-2] + arrangement[-1]
                    if (last_two == 'MI' and c == 'T') or (last_two == 'TI' and c == 'M'):
                        continue
                candidates.append((counts[c], c))
            if not candidates:
                arrangement = None
                break

            candidates.sort(reverse=True)
            chosen = candidates[0][1]
            arrangement.append(chosen)
            counts[chosen] -= 1
        if arrangement:
            results.append(('YES', ''.join(arrangement)))
        else:
            results.append(('NO', None))
    return results


T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
answers = busy_beaver_arrangement(test_cases)
for res, arrangement in answers:
    print(res)
    if arrangement:
        print(arrangement)
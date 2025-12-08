import sys
import math


def validate_candidate(x, arr):
    found_multiple = False
    found_divisor = False

    for val in arr:
        if not (x % val == 0 or val % x == 0):
            return False
        if x % val == 0:
            found_multiple = True
        if val % x == 0:
            found_divisor = True

    return found_multiple and found_divisor


def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    idx = 1
    output = []

    for _ in range(t):
        n = int(input_data[idx]);
        idx += 1
        arr = list(map(int, input_data[idx:idx + n]))
        idx += n

        arr.sort()

        prefix_lcm = [0] * n
        suffix_gcd = [0] * n

        prefix_lcm[0] = arr[0]
        for i in range(1, n):
            prefix_lcm[i] = prefix_lcm[i - 1] * arr[i] // math.gcd(prefix_lcm[i - 1], arr[i])
            if prefix_lcm[i] > 10 ** 18:  # safeguard against overflow
                prefix_lcm[i] = 10 ** 18 + 1

        suffix_gcd[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            suffix_gcd[i] = math.gcd(suffix_gcd[i + 1], arr[i])

        found = False

        # Check split points for candidates = prefix_lcm[i]
        for i in range(n - 1):
            candidate = prefix_lcm[i]
            if candidate <= 0:
                continue
            if suffix_gcd[i + 1] % candidate == 0:
                if validate_candidate(candidate, arr):
                    output.append(str(candidate))
                    found = True
                    break

        if found:
            continue

        # Check if min element works
        min_val = arr[0]
        if validate_candidate(min_val, arr):
            output.append(str(min_val))
            continue

        # Check if max element works
        max_val = arr[-1]
        if validate_candidate(max_val, arr):
            output.append(str(max_val))
            continue

        output.append("-1")

    print("\n".join(output))


if __name__ == "__main__":
    solve()

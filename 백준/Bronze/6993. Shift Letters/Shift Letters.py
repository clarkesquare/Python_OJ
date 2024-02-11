for _ in range(int(input())):
    n, m = input().split()
    m = int(m)

    print(f"Shifting {n} by {m} positions gives us: {n[-1 * m::] + n[:-1 * m]}")
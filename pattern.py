def print_pattern_E(n):
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n // 2 or i == n - 1) or (j == 0):
                print("*", end="")
            else:
                print(" ", end="")
        print()


size = 7
print_pattern_E(size)



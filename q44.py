rows = 5

for i in range(1, rows + 1):
    # Print numbers increasing from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")
    # Print numbers decreasing from i-1 back to 1
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()  # move to next line
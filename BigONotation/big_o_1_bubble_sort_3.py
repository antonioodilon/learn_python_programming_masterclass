def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n = len(data)

    comparison_count = 0
    for i in range(n - 1):
        # for j in range(n - 1):  # Old code
        for j in range(n - 1 - i):  # Making an improvement
            comparison_count += 1  # With our improvement the inner loop goes
            # around one less time
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        print(f"End of pass {i}. 'data' is now {data}")
    print(f"comparison_count is {comparison_count}")


# Trying with a much bigger list
# numbers = list(range(100, 0, -1))
numbers = [1, 2, 3, 4, 5, 9, 10, 8, 6, 7]

print(f"Sorting {numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")

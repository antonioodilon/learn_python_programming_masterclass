# Improving our algorithm


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


numbers = [15, 12, 10, 19, 20, 11, 17, 16, 14, 13, 18]

print(f"Sorting {numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")
# comparison_count went from 100 to 55

print("=" * 80)

numbers_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f"Sorting {numbers_2}")
bubble_sort(numbers_2)
print(f"The sorted data is {numbers_2}")
# comparison_count went from 100 to 55
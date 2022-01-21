def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n = len(data)
    comparison_count = 0
    for i in range(n - 1):
        swapped = False  # Added this code to deal with a list of numbers whose
        # values are already largely sorted.
        for j in range(n - 1 - i):
            comparison_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if swapped:  # We are checking if numbers have been swapped. If so,
            # the loop continues. If no numbers have been swapped, though,
            # then there is no point for the loop to continue and we break
            # out of it.
            break
        print(f"End of pass {i}. 'data' is now {data}")
    print(f"comparison_count is {comparison_count}")


numbers = [1, 2, 3, 4, 5, 9, 10, 8, 6, 7]

print(f"Sorting {numbers}")
bubble_sort(numbers)
# Without the swapped code, comparison_count was 45. With it, though, it went
# down to 9.
print(f"The sorted data is {numbers}")
# A bubble sort is a very simple algorithm and isn't used in real applications


def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n = len(data)
    # Function calls take longer to execute than getting the value of a variable.
    # So if you're going to use a function's return value more than once, then
    # bing a variable to the result of the function.

    comparison_count = 0
    for i in range(n - 1):
        for j in range(n - 1):
            comparison_count += 1  # comparison_count is how many times the
            # algorithm performed a comparison
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]  # Python always
                # evaluates the right hand side before performing an assignment
        print(f"End of pass {i}. 'data' is now {data}")
    print(f"comparison_count is {comparison_count}")


numbers = [15, 12, 10, 19, 20, 11, 17, 16, 14, 13, 18]

print(f"Sorting {numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")

print("=" * 80)

# This algorithm is not efficient at all, as can be seen. Let's create another
# list with the items sorted in reverse order. This list also contains 11 items

numbers_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f"Sorting {numbers_2}")
bubble_sort(numbers_2)
print(f"The sorted data is {numbers_2}")

# In the output we can see that in both situations comparison_count was 100.
# Shouldn't have been like this, but this is especially true with numbers_2,
# as the items are in reverse order













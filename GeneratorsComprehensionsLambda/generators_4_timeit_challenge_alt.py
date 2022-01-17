# Another way of approaching the challenge:
import timeit


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    print("Output for fact(): ")
    print(timeit.timeit("x = fact(130)", setup="from __main__ import fact", number=10000))
    print("-" * 60)
    print("Output for factorial(): ")
    print(timeit.timeit("x = factorial(130)", setup="from __main__ import factorial", number=10000))
    print("-" * 60)
    print("Output for fact() using timeit.repeat(): ")
    print(timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000, repeat=5))
    print("-" * 60)
    print("Output for factorial() using timeit.repeat(): ")
    print(timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=10000, repeat=5))

    # Again: don't try to use statistical analysis here, like calculating the
    # mean of each results, because there are so many variables in a computer
    # interfering in the result of the performance, that it is virtually
    # impossible to account for all of them. Use common sense instead

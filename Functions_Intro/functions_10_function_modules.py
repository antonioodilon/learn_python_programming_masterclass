# 1 Documentation for multiply() in 1_functions_intro.py
def multiply():
    """
    This function creates a variable called `result`. This variable
    multiplies the `int` 23 and the `float` 0.9. It then returns the
    `result` to the global scope. No parameters exist.

    :return: Returns the value of the variable `result`, which is a float
    """
    result = 23 * 0.9
    return result


# Function annotations are very useful. See video 161. Function annotations
# and type hints
def multiply_alt(x: float, y: float) -> float:
    result = x * y
    return result


# 2 Documentation for is_palindrome(string) in 3_palindrome_2.py
def is_palindrome(string: str) -> None:
    """
    This function detects if a certain word is a palindrome, that is, if
    it reads forwards same way as it reads backwards. It takes the parameter
    `string`, and it detects if the user's string, being read from the end
    to the beginning and taking steps of -1 (minus one), equals the string
    being read forwards. At the same time, it also ignores any uppercase
    letters. `If` this condition evaluates to true, the function prints that
    the string is a palindrome. `Else`, it prints that the string isn't a
    palindrome.

    :param string: When the user calls the function, s/he has to also
    call the input function in order to insert a string.
    :return: None
    """
    if string[::-1].casefold() == string.casefold():
        print("'{}' is a palindrome".format(string))
    else:
        print("'{}' is not a palindrome".format(string))


# 3 Documentation for banner_text(text) in 8_handl_invalid_default_parameter_values.py
def banner_text(text: str, banner_width: int = 80) -> int:
    """
    The user can use this function to create a banner in the output. There
    are two parameters: `text` and `banner_width`. `text` is obligatorily
    a string that can be inserted when the user calls the function. `banner_width`
    is set to the default value of 80, but can be changed by the user.
    `If` the length of `text` is greater than `banner_width` minus 4, a warning
    message appears in the output and `ValueError` is `raised`. `If` `text`
    equals the string '*', the function prints `text` multiplied by the
    width of the banner. `Else`, the function creates a variable called
    `output_string` which equals the parameter `text` with two asterisks
    (*) on either side; `text` takes place at the center of the output
    using the center() function, which in turn takes the parameter of
    `banner_width` minus the value of 4. This `else` statement prints
    `output_string`. Finally, the function returns `banner_width` to the
    global scope.

    :param text: Has no default value. User has to type it when calling
    the function.
    :param banner_width: Set to the default value of 80. Can be changed
    by the user.
    :raises ValueError: Raises an error if `text` is greater than `banner_width`.
    `Prints` a text containing `text` and `banner_width` warning the user.
    :return: Returns `banner_width` to the global scope.
    """
    if len(text) > banner_width - 4:
        raise ValueError("The length of the string {0} is bigger than the "
                         "screen width {1}".format(text, banner_width))
    if text == "*":
        print("*" * banner_width)
    else:
        output_string = "**{0}**".format(text.center(banner_width - 4))
        print(output_string)
    return banner_width


# 4 Documentation for def_fibonacci in 11_fibonacci_numbers.py
def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number for a positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result
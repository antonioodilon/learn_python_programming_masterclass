# Raw strings can be useful if you need Python to ignore what backslashes ( / )
# do.

regular_string = "this is\t a string, \and it is\n not raw"
print(regular_string)

raw_string = r"this is\t a string, \and it is\n raw"
print(raw_string)

# Notice in the example below how you need to type two backslashes in order
# to remove the error. Otherwise, Python will ignore the final quotation
# mark in the end.
error_string = r"this string can produce an error\\"
print(error_string)
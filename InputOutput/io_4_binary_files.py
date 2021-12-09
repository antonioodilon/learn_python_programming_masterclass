# bw: b = binary ; w = write
# with open("binary", "bw") as bin_file:
#     for i in range(21):
#         bin_file.write(bytes([i]))  # Converting the i numbers to a byte format
#         # Also, we are passing a list, hence [i]

# This is the better way to write the previous code
with open("binary", "bw") as bin_file:
    bin_file.write(bytes(range(21)))

# br: b = binary ; r = read
with open("binary", "br") as bin_file_2:
    for b in bin_file_2:
        print(b)

# binary files aren't written or read in the "traditional" sense, the way
# a regular text file does
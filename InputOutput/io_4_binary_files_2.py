# Storing variables in our binary files
a = 65534  # FF FE
b = 65535  # FF FF
c = 65536  # 00 01 00 00
x = 2998302  # 00 2D C0 1E

with open("binary_2", "bw") as bin_file_2:
    bin_file_2.write(a.to_bytes(2, "big"))
    bin_file_2.write(b.to_bytes(2, "big"))
    bin_file_2.write(c.to_bytes(4, "big"))
    bin_file_2.write(x.to_bytes(4, "big"))
    bin_file_2.write(x.to_bytes(4, "little"))
# Converting an integer to bytes using the to_bytes method.
# The first parameter (2 and 4) are the number of bytes

# Now we are going to read the information in the binary_2 file back.
# e = a , f = b , g = c , h = x, and i =
# int converts into an integer. Also, we need to call the .read() method
# to be able to read the file
with open("binary_2", "br") as bin_file_2:
    e = int.from_bytes(bin_file_2.read(2), "big")
    print(e)
    f = int.from_bytes(bin_file_2.read(2), "big")
    print(f)
    g = int.from_bytes(bin_file_2.read(4), "big")
    print(g)
    h = int.from_bytes(bin_file_2.read(4), "big")
    print(h)
    i = int.from_bytes(bin_file_2.read(4), "big")
    print(i)
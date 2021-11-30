import hashlib

print(sorted(hashlib.algorithms_guaranteed))
print(sorted(hashlib.algorithms_available))

print("-" * 60)

my_program = """for i in range(0, 21, 2):
print(i)
"""

print(my_program)

print("-" * 60)

for b in my_program.encode('utf8'):
    print(b, chr(b))

print("-" * 60)

original_hash = hashlib.sha256(my_program.encode('utf8'))
print(f"SHA256: {original_hash.hexdigest()}")
print(f"SHA256: {original_hash}")

print("-" * 60)

# Now we are going to modify my_program, generate a hash and check if it matches
# the previous hash, on line 21

my_program += "print('program modification')"
print(my_program)

new_hash = hashlib.sha256(my_program.encode('utf8'))
print(f"SHA256: {new_hash.hexdigest()}")
print(f"SHA256: {new_hash}")

if new_hash == original_hash:
    print("The file hasn't been modified")
else:
    print("The file has been modified, and may no longer be supported by its "
          "original creators")
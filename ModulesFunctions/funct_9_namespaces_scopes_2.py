import os


def list_directories(s):

    def dir_list(d):
        nonlocal tab_stop  # Different from global keyword. It is telling
        # Python to look for the variable in the enclosing scope (in the
        # function list_directories, which encloses dir_list).
        # If the variable was global, it would have been present in the main
        # code, outside of list_directories
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + " does not exist")


list_directories("R:\Antonio\Filmes")

print("-" * 80)

# The code above is a better way of doing what is being done in the code below
# listing = os.walk("R:\Antonio\Filmes")
#
# for root, directories, files_2 in listing:
#     print(root)
#     for directory in directories:
#         print(directories)
#     print("-" * 40)
#     for file_2 in files_2:
#         print(files_2)
#     print("-" * 40)
# Working with generators and directories
import os

root = "music"

# the os.walk() function is actually a generator that yields the next value
# os.walk() retrieves the files from a directory tree by walking through it
for path_files, directories, files in os.walk(root, topdown=True):
    if files:
        print(path_files)
        # os.path is a module that can be used to retrieve path names in Python
        first_split = os.path.split(path_files)
        print(first_split)
        # os.path.split() is a method that splits the path name into two parts:
        # a head and a tail
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            # Retrieving the name of each file starting in the beginning of
            # the name and up to, but not including, the last 5 characters,
            # which are the .emp3 extension.
            song_details = f[:-5].split(" - ")
            print(song_details)
        print("-" * 50)

    # Using the trick we've learned to get the next value by typing an input
    # every time.
    # print(path)
    # print(directories)
    # print(files)
    # input()

    # for file in files:
    #     print("\t{}".format(file))
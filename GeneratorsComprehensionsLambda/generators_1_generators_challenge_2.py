# Generators, as can be seen, are incredibly useful for many applications.
# Google, for example, displays results of a search to the user one page
# at a time instead of the thousands of pages at once, which would eat up
# all the memory from a user's computer.

import os
import fnmatch
import id3reader_p3 as id3reader
# The id3reader_p3 module is useful for reading tags of the songs


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            # absolute_path = os.path.abspath(path)  # If we want the full
            # path, we can use the .abspath() method
            yield os.path.join(path, file)
            # yield os.path.join(absolute_path, file)


error_list = []
for f in find_music('R:\Antonio\Musikk\\3 Kraftwerk', 'mp3'):
# Putting two \\ so that Python ignores one of the backslashes
# for f in find_music('music', 'emp3'):
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {0}, Album: {1}, Track: {2}, Song: {3}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
            ))
    except:
        # Sometimes it is a good idea to handle all errors and being very
        # broad
        error_list.append(f)
    # except OSError:
    #     print("An error has occurred on your operating system")
    # except Exception:
    #     print("An unknown error has occurred")

for error_file in error_list:
    print(error_file)
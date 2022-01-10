import os
import fnmatch


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            # absolute_path = os.path.abspath(path)  # If we want the full
            # path, we can use the .abspath() method
            yield os.path.join(path, file)
            # yield os.path.join(absolute_path, file)


for f in find_music('R:\Antonio\Musikk\\3 Kraftwerk', 'mp3'):
    # Putting two \\ so that Python ignores one of the backslashes
    print(f)
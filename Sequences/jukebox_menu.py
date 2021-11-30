from nested_data_albums_list import albums

# Constants are all in uppercase. See constants.py file
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Let's Rock and Roll! Choose an artist's album and then a song"
          " (invalid choice exits the jukebox)")
    for index, (album, artist, year, song) in enumerate(albums):
        # We use enumerate() to get the index
        print("{0}: {1}".format(index + 1, album))
    user_choice = int(input())
    if 1 <= user_choice <= len(albums):
        songs_list = albums[user_choice - 1][SONGS_LIST_INDEX]
    else:
        break
    print("Now choose your song:")
    for index, (track_number, song_title) in enumerate(songs_list):
        print("{0} : {1}".format(track_number, song_title))
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Now playing: {}".format(title))
        print("="*40)
    else:
        break
    # Alternatively, you could write this for loop in the while True loop:
    # for index, value in enumerate(albums):
    #     album, artist, year, song = value
    #     print(index + 1, album, artist, year, song)


# while True:
#     print("Let's Rock and Roll! Choose an artist's album and then a song.")
#     user_choice = int(input("First, choose an album. Type a number from 1 to 4: {}".
#                         format(albums)))
#     if 1 <= user_choice >= 4:
#         user_choice2 = int(input("Now choose a song from the album {}"
#                                 .format(user_choice)))
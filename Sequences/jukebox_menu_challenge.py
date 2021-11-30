from nested_data_albums_list import albums

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
    print("Now choose your song. If you enter an invalid choice, the"
          " available albums will be displayed again.")
    for index, (track_number, song_title) in enumerate(songs_list):
        print("{0} : {1}".format(track_number, song_title))
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Now playing: {}".format(title))
    print("="*40)
    # All you have to do is remove the else: break block

    # Another solution:
    # else:
    #     print("="*40)
    #     pass  # I can't believe this was so easy...
# Starting sqlite3:
# 1) Command prompt, type sqlite3
# 2) Press .quit and create a database: type sqlite3 test.db (Can be any name
# not only test)
# 3) .headers on , then: CREATE TABLE contacts (name text, phone integer, email text);
# Don't forget the semicolons ; ! Very important
# In sqlite, if you do something wrong, it warns you; otherwise, it just
# keeps quiet
# 4) Inserting values: INSERT INTO contacts (name, phone, email) VALUES ('Antonio', 123456, 'antonio@myemail.com');
# 5) To check if all the values have been inserted: SELECT * FROM contacts;
    # Remember the spaces between SELECT and FROM
    # Another way to do the same thing: SELECT name, phone, email FROM contacts;
    # Or SELECT name, phone FROM contacts;
    # If you type, for example, SELECT name FROM and don't type the rest,
    # three dots and a > sign will appear, and sqlite will let you type
    # what's missing. For example:
    # SELECT name FROM
    # ...> contacts;
# 6) To type new values, you can do it like this:
    # INSERT INTO contacts (name, phone, email) VALUES ('Maria', 789012, 'maria@myemail.com');
    # or like this: INSERT INTO contacts VALUES ('Maria', 789012, 'maria@myemail.com');
# If you want to insert values only on specific fields:
# 7) To open a previous file type .open test.db
    # Then SELECT * FROM contacts;
# 8) In sqlite, it is possible to insert objects of one type in a field
# that expects another data type, but one shouldn't do that, because may
# very well cause problems.
# 9) To update a database in sqlite, one can write UPDATE contacts SET email="luiza@email.com";
# 10) However, if you do this, it will change everyone's email to luiza@email.com;
# Therefore, make sure to back up the database first, by typing .backup testbackup (without ; )
# That way, if you accidentally change everything, you can type .restore testbackup
# 11) To change only one particular entry: UPDATE contacts set email="antoinette
# 12) If you want to select just some pieces of information for a particular entry:
# SELECT * FROM contacts WHERE name='Antonio';
# or SELECT phone, email FROM contacts WHERE name='Antonio';
# 13) To delete an entry, BE CAREFUL! Make sure to back the database first
# before deleting anything! DELETE FROM contacts WHERE phone=98765;
# 14) .tables to show the tables of our database
# 15) .schema to show the original command used to create a table. Output is
# something like: CREATE TABLE contacts (name text, phone integer, email text);
# 16) .dump to show the statements we used to create the tables and insert
# the data that is in it. Output below:
"""PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE contacts (name text, phone integer, email text);
INSERT INTO contacts VALUES('Antonio',123456,'antonio@myemail.com');
INSERT INTO contacts VALUES('Maria',789012,'maria@heremail.com');
INSERT INTO contacts VALUES('Antoinette',34567,'antoinette@antuemail.com');
INSERT INTO contacts VALUES('Ionete',1234,'ionete@heremail.com');
COMMIT;"""
# 17) .exit takes you back to C:\Users\Antônio Madureira>

# To open a new location: cd Desktop
# And the type sqlite3
# 18) When creating tables and databases in sqlite, think about whether
# or not it makes sense to create an entry with a NOT NULL value. For example,
# here in Brazil a lot of people have big names, and thus have middle names,
# but it isn't so in many other countries. Therefore, it may make sense
# to create a table to allow a NULL value in the middle name section.
# 19) To automatically insert a value in our database without needing to
# specify the id: INSERT INTO artists (name) VALUES('Karolina Cicha');

# 20) To ORDER BY using a certain parameter: SELECT * FROM artists ORDER BY name;
# 21: To ORDER BY ignoring lower and upper case:
# SELECT * FROM albums ORDER BY name COLLATE NOCASE;
# 22) To ORDER BY ascending or descending order:
# SELECT * FROM albums ORDER BY name COLLATE NOCASE DESC; (or ASC)
# 23) If we want to group the albums by artist, for example:
# SELECT * FROM albums ORDER BY artist, name COLLATE NOCASE;
# 24) Mini challenge: selecting the songs, grouping them by the album and
# making the songs appear in correct order:
# SELECT * FROM songs ORDER BY album, track COLLATE NOCASE;
# If you ORDER BY track, album, the output will not be what you expect

# 25) Joining tables together:
# SELECT songs.track, songs.title, albums.name FROM songs JOIN albums ON songs.album = albums._id;
# 26) Joining tables together and ordering by album and track:
# SELECT songs.track, songs.title, albums.name FROM songs JOIN albums ON songs.album = albums._id ORDER BY albums.name, songs.track;
# CAREFUL! Some column names are shared between two different tables! For example, _id
# 27) Better to specify with INNER JOIN:
# SELECT songs.track, songs.title, albums.name FROM songs INNER JOIN albums ON songs.album = albums._id ORDER BY albums.name, songs.track;
# SELECT songs.track, songs.title, albums.name FROM songs INNER JOIN albums ON songs.album = albums._id ORDER BY albums.name, songs.track COLLATE NOCASE;
# 28) Looks better if we show the album name first:
# SELECT albums.name, songs.track, songs.title FROM songs INNER JOIN albums ON songs.album = albums._id ORDER BY albums.name, songs.track;

# 29) Listing the artists with their albums and ordering by the artists' name
# in alphabetical order:
# SELECT artists.name, albums.name FROM artists INNER JOIN albums ON albums.artist = artists._id ORDER BY artists.name, albums.name;

# 30) Listing the artists, albums and songs:
# SELECT artists.name, albums.name, songs.track, songs.title FROM artists INNER JOIN albums ON albums.artist = artists._id INNER JOIN songs ON songs.album = albums._id ORDER BY artists.name, albums.name, songs.track;

# 31) Filtering for the album Argus
# WHERE needs to come before ORDER BY!
# SELECT artists.name, albums.name, songs.track, songs.title FROM artists INNER JOIN albums ON albums.artist = artists._id INNER JOIN songs ON songs.album = albums._id WHERE albums.name = 'Argus' ORDER BY artists.name, albums.name, songs.track;

# SELECT artists.name, albums.name, songs.track, songs.title
# FROM artists INNER JOIN albums ON albums.artist = artists._id
# INNER JOIN songs ON songs.album = albums._id WHERE albums._id = 60
# ORDER BY artists.name, albums.name, songs.track;

# 32) Now let's say that I want a song, but I don't remember the exact name,
# or the artist's or album's. I just know that it has the word "femme":
"""SELECT artists.name, albums.name, songs.track, songs.title
FROM artists INNER JOIN albums ON albums.artist = artists._id
INNER JOIN songs ON songs.album = albums._id WHERE songs.title LIKE '%femme%'
ORDER BY artists.name, albums.name, songs.track;"""
# LIKE is not case sensitive
"""SELECT artists.name, albums.name, songs.track, songs.title
FROM artists INNER JOIN albums ON albums.artist = artists._id
INNER JOIN songs ON songs.album = albums._id WHERE songs.title LIKE '%rock%'
ORDER BY artists.name, albums.name, songs.track;"""

"""SELECT artists.name, albums.name, songs.track, songs.title
FROM artists INNER JOIN albums ON albums.artist = artists._id
INNER JOIN songs ON songs.album = albums._id WHERE artists.name LIKE '%jefferson%'
ORDER BY artists.name, albums.name, songs.track;"""

#Creating a VIEW using this command:
"""CREATE VIEW artist_list AS
SELECT artists.name, albums.name, songs.track, songs.title
FROM artists INNER JOIN albums ON albums.artist = artists._id
INNER JOIN songs ON songs.album = albums._id
ORDER BY artists.name, albums.name, songs.track;"""
# If you type .schema, you will see that artist_list is there and can be
# manipulated like a normal table in our database. For example:
# SELECT * FROM artist_list WHERE name LIKE '%jefferson%';
# SELECT * FROM artist_list WHERE title LIKE '%rock%';
# To delete a view: DROP VIEW artist_list;

# Since we had name referring to artist and name referring to album, let's
# give artists.name an alias of artist and albums.name an alias of album
"""CREATE VIEW artist_list AS
SELECT artists.name AS artist, albums.name AS album, songs.track, songs.title
FROM artists INNER JOIN albums ON albums.artist = artists._id
INNER JOIN songs ON songs.album = albums._id
ORDER BY artists.name, albums.name, songs.track;"""
# Now we can do things like:
# SELECT * FROM artist_list WHERE artist LIKE '%jefferson%';

# Selecting all from artist_list where track is not equal to 1:
# SELECT * FROM artist_list WHERE track <> 1;

# The count of all the songs we have:
# SELECT count(*) FROM songs;

# My solution to the challenge in class 332:
"""
1) SELECT * FROM albums INNER JOIN songs ON songs.album = albums._id 
WHERE albums.name = 'Forbidden';

2) SELECT * FROM albums INNER JOIN songs ON songs.album = albums._id 
WHERE albums.name = 'Forbidden' ORDER BY songs.track;
SELECT songs.track, songs.title

3) SELECT * FROM artists INNER JOIN albums ON albums.artist = artists._id 
INNER JOIN songs ON songs.album = albums._id WHERE artists.name = 'Deep Purple' 
ORDER BY albums.name, songs.track;

4) UPDATE artists SET name = 'Friendly Fire' WHERE name = 'Mehitabel';

5) SELECT * FROM artists WHERE name = 'Friendly Fire';

6) SELECT title FROM songs INNER JOIN albums ON songs.album = albums._id 
INNER JOIN artists on albums.artist = artists._id WHERE artists.name = 'Aerosmith' 
ORDER BY songs.title;

7) SELECT count(title) FROM songs INNER JOIN albums ON songs.album = albums._id
 INNER JOIN artists on albums.artist = artists._id WHERE artists.name = 'Aerosmith' 
 ORDER BY songs.title;

8) SELECT DISTINCT title FROM songs INNER JOIN albums ON songs.album = albums._id 
INNER JOIN artists on albums.artist = artists._id WHERE artists.name = 'Aerosmith' 
ORDER BY songs.title;

9) SELECT count(DISTINCT title) FROM songs INNER JOIN albums ON songs.album = albums._id 
INNER JOIN artists on albums.artist = artists._id WHERE artists.name = 'Aerosmith' 
ORDER BY songs.title;

10a) SELECT count(DISTINCT artists.name) FROM songs INNER JOIN 
albums ON songs.album = albums._id INNER JOIN artists on albums.artist = artists._id 
WHERE artists.name = 'Aerosmith' ORDER BY songs.title;

10b) SELECT count(DISTINCT albums.name) FROM songs INNER JOIN albums 
ON songs.album = albums._id INNER JOIN artists on albums.artist = artists._id 
WHERE artists.name = 'Aerosmith' ORDER BY songs.title;
"""






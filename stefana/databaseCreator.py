import sqlite3

conn = sqlite3.connect('music.db')

c = conn.cursor()

#create table music

c.execute("CREATE TABLE music (musicId integer primary key, artist varchar2(100), songTitle varchar2(100), genre varchar2(100), musicData text)")


#create table notes

#c.execute("CREATE TABLE notes (notesId integer primary key, musicId integer foreign key, )")

#create table score

c.execute("CREATE TABLE score (scoreId integer primary key, musicId integer, lyricsComplexity integer, notesComplexity integer, foreign key(musicId) references music(musicId))")

#create table words

c.execute("CREATE TABLE words (wordId integer primary key, wordName varchar2(100), scorGeneral integer)")
conn.commit()
conn.close()
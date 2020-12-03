# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL REFERENCES time(start_time),
    user_id INT NOT NULL,
    level VARCHAR (4),
    song_id VARCHAR (50) REFERENCES songs(song_id),
    artist_id VARCHAR (50) REFERENCES artists(artist_id),
    session_id SMALLINT,
    location VARCHAR (100),
    user_agent VARCHAR (200),
        FOREIGN KEY(user_id) 
        REFERENCES users(user_id)
        ON DELETE CASCADE
    )
""")
#
user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id SMALLINT PRIMARY KEY,
    first_name VARCHAR (50), 
    last_name VARCHAR (50),
    gender VARCHAR (6),
    level VARCHAR (4) 
    )
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR (50) PRIMARY KEY,
    title VARCHAR (100), 
    Artist_id VARCHAR (50) NOT NULL,
    year SMALLINT,
    duration FLOAT (5)
    )
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR (50) PRIMARY KEY,
    name VARCHAR (100),
    location VARCHAR (50),
    latitude NUMERIC,
    longitute NUMERIC
    )
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY,
    hour SMALLINT,
    day SMALLINT,
    week SMALLINT,
    month SMALLINT,
    year SMALLINT,
    weekday SMALLINT
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (
    start_time, 
    user_id, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent 
    )
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT
DO NOTHING;
""")


user_table_insert = ("""
INSERT INTO users (
    user_id, 
    first_name,
    last_name, 
    gender, 
    level 
    )
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) 
DO UPDATE 
SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (
    song_id,
    title,
    artist_id,
    year,
    duration
    ) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT
DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (
    artist_id,
    name,
    location, 
    latitude, 
    longitute 
    ) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT
DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (
    start_time,
    hour, 
    day, 
    week, 
    month, 
    year, 
    weekday
    )
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT
DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, s.artist_id
FROM songs s
INNER JOIN  artists a
ON s.artist_id = a.artist_id
WHERE s.title = %s
AND  a.name = %s AND  s.duration = %s;
""")


# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,  songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
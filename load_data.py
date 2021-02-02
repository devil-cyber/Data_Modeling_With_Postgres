import psycopg2
conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=mani360@")
cur = conn.cursor()
cur.execute("""
    SELECT s.song_id, a.artist_id,a.name,s.title
    FROM songs s
    JOIN artists a ON s.artist_id = a.artist_id
""")

row = cur.fetchone()
while(row):
    print(row)
    row = cur.fetchone()
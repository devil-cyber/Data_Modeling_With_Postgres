import psycopg2
from sql_queries import create_table_queries,drop_table_queries

def create_database():
    #connect to default database
    conn = psycopg2.connect('host=127.0.0.1 dbname=udacity user=postgres password=mani360@')
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute('DROP DATABASE IF EXISTS sparkifydb')
    cur.execute('CREATE DATABASE sparkifydb')
    conn.close()
    # connect to the new database
    conn = psycopg2.connect('host=127.0.0.1 dbname=sparkifydb user=postgres password=mani360@')
    cur = conn.cursor()
    return conn, cur

def drop_table(conn,cur):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_table(conn,cur):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    conn, cur = create_database()
    drop_table(conn,cur)
    create_table(conn,cur)
    conn.close()

if __name__ == '__main__':
    main()

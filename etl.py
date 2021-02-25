import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Description :  
    - Executes each query in the copy_table_queries list from sql_queries.py to copy data from S3 buckets to staging tables:
      staging_events, staging_songs    
    - Finally, closes the connection. 
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Description :  
    - Executes each query in the list insert_table_queries defined in sql_queries.py to insert distinct data into final tables:
      Fact Table : fact_songplay
      Dimension Tables : dim_user, dim_song, dim_artist, dim_time    
    - Finally, closes the connection. 
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Description :  
    - Establishes connection with the sparkify database and gets cursor to it.    
    - Calls load_staging_tables function to extract and copy log_data and song_data from S3 buckets to staging tables.
    - Calls insert_tables function to process transformed data into final analytics tables.
    - Finally, closes the connection. 
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
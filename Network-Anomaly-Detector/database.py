import sqlite3

def save_anomaly(df):
    conn = sqlite3.connect('logs.db')

    # Save DataFrame to table named threats
    # Check for previous data so not overwriting previously written data
    df.to_sql('threats', conn, if_exists='append', index=False)

    conn.close()

import sqlite3
import pandas as pd

def view_database():
    # Connect to the database
    conn = sqlite3.connect('ipl_betting.db')
    
    # Read the bets table into a pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM bets", conn)
    
    # Display the contents
    print("\n=== IPL Betting Database Contents ===")
    if len(df) == 0:
        print("No bets found in the database.")
    else:
        print(df)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    view_database() 
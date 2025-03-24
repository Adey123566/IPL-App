import sqlite3
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def init_db():
    """Initialize the database with required tables"""
    conn = sqlite3.connect('ipl_betting.db')
    c = conn.cursor()
    
    # Create bets table
    c.execute('''
        CREATE TABLE IF NOT EXISTS bets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            match TEXT NOT NULL,
            amount REAL NOT NULL,
            team TEXT NOT NULL,
            username TEXT NOT NULL,
            opponent TEXT,
            date TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    logger.info("Database initialized successfully")

def add_bet(match, amount, team, username, opponent=None):
    """Add a new bet to the database"""
    logger.debug(f"Attempting to add bet to database: match={match}, amount={amount}, team={team}, username={username}, opponent={opponent}")
    conn = sqlite3.connect('ipl_betting.db')
    c = conn.cursor()
    
    try:
        c.execute('''
            INSERT INTO bets (match, amount, team, username, opponent, date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (match, amount, team, username, opponent, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        conn.commit()
        bet_id = c.lastrowid
        logger.info(f"Bet added successfully with ID: {bet_id}")
        return True, bet_id
    except Exception as e:
        logger.error(f"Error adding bet to database: {str(e)}")
        return False, None
    finally:
        conn.close()

def get_all_bets():
    """Retrieve all bets from the database"""
    conn = sqlite3.connect('ipl_betting.db')
    c = conn.cursor()
    
    try:
        c.execute('SELECT * FROM bets ORDER BY date DESC')
        bets = c.fetchall()
        
        # Convert to list of dictionaries
        bet_list = []
        for bet in bets:
            bet_list.append({
                'id': bet[0],
                'match': bet[1],
                'amount': bet[2],
                'team': bet[3],
                'username': bet[4],
                'opponent': bet[5],
                'date': bet[6]
            })
        
        logger.info(f"Retrieved {len(bet_list)} bets from database")
        return bet_list
    except Exception as e:
        logger.error(f"Error retrieving bets: {str(e)}")
        return []
    finally:
        conn.close() 
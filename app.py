from flask import Flask, render_template, request, jsonify
import logging
from database import init_db, add_bet, get_all_bets
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize database
init_db()

# List of IPL 2025 fixtures
fixtures = [
    {
        "id": 1,
        "team1": "Chennai Super Kings",
        "team2": "Royal Challengers Bangalore",
        "date": "2025-03-22",
        "time": "19:30",
        "venue": "M.A. Chidambaram Stadium, Chennai"
    },
    {
        "id": 2,
        "team1": "Punjab Kings",
        "team2": "Delhi Capitals",
        "date": "2025-03-23",
        "time": "15:30",
        "venue": "Punjab Cricket Association Stadium, Mohali"
    },
    {
        "id": 3,
        "team1": "Kolkata Knight Riders",
        "team2": "Sunrisers Hyderabad",
        "date": "2025-03-23",
        "time": "19:30",
        "venue": "Eden Gardens, Kolkata"
    },
    {
        "id": 4,
        "team1": "Rajasthan Royals",
        "team2": "Lucknow Super Giants",
        "date": "2025-03-24",
        "time": "15:30",
        "venue": "Sawai Mansingh Stadium, Jaipur"
    },
    {
        "id": 5,
        "team1": "Mumbai Indians",
        "team2": "Gujarat Titans",
        "date": "2025-03-24",
        "time": "19:30",
        "venue": "Wankhede Stadium, Mumbai"
    },
    {
        "id": 6,
        "team1": "Royal Challengers Bangalore",
        "team2": "Kolkata Knight Riders",
        "date": "2025-03-25",
        "time": "19:30",
        "venue": "M.Chinnaswamy Stadium, Bangalore"
    },
    {
        "id": 7,
        "team1": "Lucknow Super Giants",
        "team2": "Punjab Kings",
        "date": "2025-03-26",
        "time": "19:30",
        "venue": "Ekana Cricket Stadium, Lucknow"
    },
    {
        "id": 8,
        "team1": "Gujarat Titans",
        "team2": "Sunrisers Hyderabad",
        "date": "2025-03-27",
        "time": "19:30",
        "venue": "Narendra Modi Stadium, Ahmedabad"
    },
    {
        "id": 9,
        "team1": "Delhi Capitals",
        "team2": "Rajasthan Royals",
        "date": "2025-03-28",
        "time": "19:30",
        "venue": "Arun Jaitley Stadium, Delhi"
    },
    {
        "id": 10,
        "team1": "Chennai Super Kings",
        "team2": "Mumbai Indians",
        "date": "2025-03-29",
        "time": "19:30",
        "venue": "M.A. Chidambaram Stadium, Chennai"
    },
    {
        "id": 11,
        "team1": "Sunrisers Hyderabad",
        "team2": "Punjab Kings",
        "date": "2025-03-30",
        "time": "15:30",
        "venue": "Rajiv Gandhi International Stadium, Hyderabad"
    },
    {
        "id": 12,
        "team1": "Gujarat Titans",
        "team2": "Royal Challengers Bangalore",
        "date": "2025-03-30",
        "time": "19:30",
        "venue": "Narendra Modi Stadium, Ahmedabad"
    },
    {
        "id": 13,
        "team1": "Kolkata Knight Riders",
        "team2": "Delhi Capitals",
        "date": "2025-03-31",
        "time": "19:30",
        "venue": "Eden Gardens, Kolkata"
    },
    {
        "id": 14,
        "team1": "Mumbai Indians",
        "team2": "Rajasthan Royals",
        "date": "2025-04-01",
        "time": "19:30",
        "venue": "Wankhede Stadium, Mumbai"
    },
    {
        "id": 15,
        "team1": "Lucknow Super Giants",
        "team2": "Chennai Super Kings",
        "date": "2025-04-02",
        "time": "19:30",
        "venue": "Ekana Cricket Stadium, Lucknow"
    },
    {
        "id": 16,
        "team1": "Punjab Kings",
        "team2": "Kolkata Knight Riders",
        "date": "2025-04-03",
        "time": "19:30",
        "venue": "Punjab Cricket Association Stadium, Mohali"
    },
    {
        "id": 17,
        "team1": "Sunrisers Hyderabad",
        "team2": "Mumbai Indians",
        "date": "2025-04-04",
        "time": "19:30",
        "venue": "Rajiv Gandhi International Stadium, Hyderabad"
    },
    {
        "id": 18,
        "team1": "Delhi Capitals",
        "team2": "Gujarat Titans",
        "date": "2025-04-05",
        "time": "15:30",
        "venue": "Arun Jaitley Stadium, Delhi"
    },
    {
        "id": 19,
        "team1": "Royal Challengers Bangalore",
        "team2": "Lucknow Super Giants",
        "date": "2025-04-05",
        "time": "19:30",
        "venue": "M.Chinnaswamy Stadium, Bangalore"
    },
    {
        "id": 20,
        "team1": "Rajasthan Royals",
        "team2": "Chennai Super Kings",
        "date": "2025-04-06",
        "time": "19:30",
        "venue": "Sawai Mansingh Stadium, Jaipur"
    },
    {
        "id": 21,
        "team1": "Mumbai Indians",
        "team2": "Punjab Kings",
        "date": "2025-04-07",
        "time": "19:30",
        "venue": "Wankhede Stadium, Mumbai"
    },
    {
        "id": 22,
        "team1": "Kolkata Knight Riders",
        "team2": "Gujarat Titans",
        "date": "2025-04-08",
        "time": "19:30",
        "venue": "Eden Gardens, Kolkata"
    },
    {
        "id": 23,
        "team1": "Sunrisers Hyderabad",
        "team2": "Delhi Capitals",
        "date": "2025-04-09",
        "time": "19:30",
        "venue": "Rajiv Gandhi International Stadium, Hyderabad"
    },
    {
        "id": 24,
        "team1": "Chennai Super Kings",
        "team2": "Rajasthan Royals",
        "date": "2025-04-10",
        "time": "19:30",
        "venue": "M.A. Chidambaram Stadium, Chennai"
    },
    {
        "id": 25,
        "team1": "Lucknow Super Giants",
        "team2": "Mumbai Indians",
        "date": "2025-04-11",
        "time": "19:30",
        "venue": "Ekana Cricket Stadium, Lucknow"
    },
    {
        "id": 26,
        "team1": "Royal Challengers Bangalore",
        "team2": "Punjab Kings",
        "date": "2025-04-12",
        "time": "15:30",
        "venue": "M.Chinnaswamy Stadium, Bangalore"
    },
    {
        "id": 27,
        "team1": "Gujarat Titans",
        "team2": "Kolkata Knight Riders",
        "date": "2025-04-12",
        "time": "19:30",
        "venue": "Narendra Modi Stadium, Ahmedabad"
    },
    {
        "id": 28,
        "team1": "Delhi Capitals",
        "team2": "Sunrisers Hyderabad",
        "date": "2025-04-13",
        "time": "19:30",
        "venue": "Arun Jaitley Stadium, Delhi"
    },
    {
        "id": 29,
        "team1": "Mumbai Indians",
        "team2": "Chennai Super Kings",
        "date": "2025-04-14",
        "time": "19:30",
        "venue": "Wankhede Stadium, Mumbai"
    },
    {
        "id": 30,
        "team1": "Rajasthan Royals",
        "team2": "Royal Challengers Bangalore",
        "date": "2025-04-15",
        "time": "19:30",
        "venue": "Sawai Mansingh Stadium, Jaipur"
    },
    {
        "id": 31,
        "team1": "Punjab Kings",
        "team2": "Lucknow Super Giants",
        "date": "2025-04-16",
        "time": "19:30",
        "venue": "Punjab Cricket Association Stadium, Mohali"
    },
    {
        "id": 32,
        "team1": "Kolkata Knight Riders",
        "team2": "Delhi Capitals",
        "date": "2025-04-17",
        "time": "19:30",
        "venue": "Eden Gardens, Kolkata"
    },
    {
        "id": 33,
        "team1": "Gujarat Titans",
        "team2": "Chennai Super Kings",
        "date": "2025-04-18",
        "time": "19:30",
        "venue": "Narendra Modi Stadium, Ahmedabad"
    },
    {
        "id": 34,
        "team1": "Sunrisers Hyderabad",
        "team2": "Mumbai Indians",
        "date": "2025-04-19",
        "time": "19:30",
        "venue": "Rajiv Gandhi International Stadium, Hyderabad"
    },
    {
        "id": 35,
        "team1": "Royal Challengers Bangalore",
        "team2": "Delhi Capitals",
        "date": "2025-04-20",
        "time": "19:30",
        "venue": "M.Chinnaswamy Stadium, Bangalore"
    },
    {
        "id": 36,
        "team1": "Lucknow Super Giants",
        "team2": "Kolkata Knight Riders",
        "date": "2025-04-21",
        "time": "19:30",
        "venue": "Ekana Cricket Stadium, Lucknow"
    },
    {
        "id": 37,
        "team1": "Punjab Kings",
        "team2": "Gujarat Titans",
        "date": "2025-04-22",
        "time": "19:30",
        "venue": "Punjab Cricket Association Stadium, Mohali"
    },
    {
        "id": 38,
        "team1": "Chennai Super Kings",
        "team2": "Sunrisers Hyderabad",
        "date": "2025-04-23",
        "time": "19:30",
        "venue": "M.A. Chidambaram Stadium, Chennai"
    },
    {
        "id": 39,
        "team1": "Rajasthan Royals",
        "team2": "Mumbai Indians",
        "date": "2025-04-24",
        "time": "19:30",
        "venue": "Sawai Mansingh Stadium, Jaipur"
    },
    {
        "id": 40,
        "team1": "Delhi Capitals",
        "team2": "Lucknow Super Giants",
        "date": "2025-04-25",
        "time": "19:30",
        "venue": "Arun Jaitley Stadium, Delhi"
    },
    {
        "id": 41,
        "team1": "Kolkata Knight Riders",
        "team2": "Royal Challengers Bangalore",
        "date": "2025-04-26",
        "time": "19:30",
        "venue": "Eden Gardens, Kolkata"
    },
    {
        "id": 42,
        "team1": "Gujarat Titans",
        "team2": "Punjab Kings",
        "date": "2025-04-27",
        "time": "19:30",
        "venue": "Narendra Modi Stadium, Ahmedabad"
    },
    {
        "id": 43,
        "team1": "Mumbai Indians",
        "team2": "Delhi Capitals",
        "date": "2025-04-28",
        "time": "19:30",
        "venue": "Wankhede Stadium, Mumbai"
    },
    {
        "id": 44,
        "team1": "Sunrisers Hyderabad",
        "team2": "Chennai Super Kings",
        "date": "2025-04-29",
        "time": "19:30",
        "venue": "Rajiv Gandhi International Stadium, Hyderabad"
    },
    {
        "id": 45,
        "team1": "Royal Challengers Bangalore",
        "team2": "Rajasthan Royals",
        "date": "2025-04-30",
        "time": "19:30",
        "venue": "M.Chinnaswamy Stadium, Bangalore"
    },
    {
        "id": 46,
        "team1": "Lucknow Super Giants",
        "team2": "Gujarat Titans",
        "date": "2025-05-01",
        "time": "19:30",
        "venue": "Ekana Cricket Stadium, Lucknow"
    },
    {
        "id": 47,
        "team1": "Punjab Kings",
        "team2": "Mumbai Indians",
        "date": "2025-05-02",
        "time": "19:30",
        "venue": "Punjab Cricket Association Stadium, Mohali"
    },
    {
        "id": 48,
        "team1": "Chennai Super Kings",
        "team2": "Kolkata Knight Riders",
        "date": "2025-05-03",
        "time": "19:30",
        "venue": "M.A. Chidambaram Stadium, Chennai"
    },
    {
        "id": 49,
        "team1": "Delhi Capitals",
        "team2": "Royal Challengers Bangalore",
        "date": "2025-05-04",
        "time": "19:30",
        "venue": "Arun Jaitley Stadium, Delhi"
    },
    {
        "id": 50,
        "team1": "Rajasthan Royals",
        "team2": "Sunrisers Hyderabad",
        "date": "2025-05-05",
        "time": "19:30",
        "venue": "Sawai Mansingh Stadium, Jaipur"
    },
    {
        "id": 51,
        "team1": "Gujarat Titans",
        "team2": "Lucknow Super Giants",
        "date": "2025-05-06",
        "time": "19:30",
        "venue": "Narendra Modi Stadium, Ahmedabad"
    },
    {
        "id": 52,
        "team1": "Mumbai Indians",
        "team2": "Kolkata Knight Riders",
        "date": "2025-05-07",
        "time": "19:30",
        "venue": "Wankhede Stadium, Mumbai"
    },
    {
        "id": 53,
        "team1": "Punjab Kings",
        "team2": "Chennai Super Kings",
        "date": "2025-05-08",
        "time": "19:30",
        "venue": "Punjab Cricket Association Stadium, Mohali"
    },
    {
        "id": 54,
        "team1": "Sunrisers Hyderabad",
        "team2": "Royal Challengers Bangalore",
        "date": "2025-05-09",
        "time": "19:30",
        "venue": "Rajiv Gandhi International Stadium, Hyderabad"
    },
    {
        "id": 55,
        "team1": "Delhi Capitals",
        "team2": "Gujarat Titans",
        "date": "2025-05-10",
        "time": "19:30",
        "venue": "Arun Jaitley Stadium, Delhi"
    },
    {
        "id": 56,
        "team1": "Rajasthan Royals",
        "team2": "Punjab Kings",
        "date": "2025-05-11",
        "time": "19:30",
        "venue": "Sawai Mansingh Stadium, Jaipur"
    },
    {
        "id": 57,
        "team1": "Chennai Super Kings",
        "team2": "Lucknow Super Giants",
        "date": "2025-05-12",
        "time": "19:30",
        "venue": "M.A. Chidambaram Stadium, Chennai"
    },
    {
        "id": 58,
        "team1": "Kolkata Knight Riders",
        "team2": "Mumbai Indians",
        "date": "2025-05-13",
        "time": "19:30",
        "venue": "Eden Gardens, Kolkata"
    },
    {
        "id": 59,
        "team1": "Royal Challengers Bangalore",
        "team2": "Sunrisers Hyderabad",
        "date": "2025-05-14",
        "time": "19:30",
        "venue": "M.Chinnaswamy Stadium, Bangalore"
    },
    {
        "id": 60,
        "team1": "Gujarat Titans",
        "team2": "Delhi Capitals",
        "date": "2025-05-15",
        "time": "19:30",
        "venue": "Narendra Modi Stadium, Ahmedabad"
    },
    {
        "id": 61,
        "team1": "Punjab Kings",
        "team2": "Rajasthan Royals",
        "date": "2025-05-16",
        "time": "19:30",
        "venue": "Punjab Cricket Association Stadium, Mohali"
    },
    {
        "id": 62,
        "team1": "Lucknow Super Giants",
        "team2": "Chennai Super Kings",
        "date": "2025-05-17",
        "time": "19:30",
        "venue": "Ekana Cricket Stadium, Lucknow"
    },
    {
        "id": 63,
        "team1": "Mumbai Indians",
        "team2": "Kolkata Knight Riders",
        "date": "2025-05-18",
        "time": "19:30",
        "venue": "Wankhede Stadium, Mumbai"
    },
    {
        "id": 64,
        "team1": "Sunrisers Hyderabad",
        "team2": "Royal Challengers Bangalore",
        "date": "2025-05-19",
        "time": "19:30",
        "venue": "Rajiv Gandhi International Stadium, Hyderabad"
    },
    {
        "id": 65,
        "team1": "Delhi Capitals",
        "team2": "Gujarat Titans",
        "date": "2025-05-20",
        "time": "19:30",
        "venue": "Arun Jaitley Stadium, Delhi"
    },
    {
        "id": 66,
        "team1": "Rajasthan Royals",
        "team2": "Punjab Kings",
        "date": "2025-05-21",
        "time": "19:30",
        "venue": "Sawai Mansingh Stadium, Jaipur"
    },
    {
        "id": 67,
        "team1": "Chennai Super Kings",
        "team2": "Lucknow Super Giants",
        "date": "2025-05-22",
        "time": "19:30",
        "venue": "M.A. Chidambaram Stadium, Chennai"
    },
    {
        "id": 68,
        "team1": "Kolkata Knight Riders",
        "team2": "Mumbai Indians",
        "date": "2025-05-23",
        "time": "19:30",
        "venue": "Eden Gardens, Kolkata"
    },
    {
        "id": 69,
        "team1": "Royal Challengers Bangalore",
        "team2": "Sunrisers Hyderabad",
        "date": "2025-05-24",
        "time": "19:30",
        "venue": "M.Chinnaswamy Stadium, Bangalore"
    },
    {
        "id": 70,
        "team1": "Gujarat Titans",
        "team2": "Delhi Capitals",
        "date": "2025-05-25",
        "time": "19:30",
        "venue": "Narendra Modi Stadium, Ahmedabad"
    },
    {
        "id": 71,
        "team1": "Punjab Kings",
        "team2": "Rajasthan Royals",
        "date": "2025-05-26",
        "time": "19:30",
        "venue": "Punjab Cricket Association Stadium, Mohali"
    },
    {
        "id": 72,
        "team1": "Lucknow Super Giants",
        "team2": "Chennai Super Kings",
        "date": "2025-05-27",
        "time": "19:30",
        "venue": "Ekana Cricket Stadium, Lucknow"
    },
    {
        "id": 73,
        "team1": "Mumbai Indians",
        "team2": "Kolkata Knight Riders",
        "date": "2025-05-28",
        "time": "19:30",
        "venue": "Wankhede Stadium, Mumbai"
    },
    {
        "id": 74,
        "team1": "Sunrisers Hyderabad",
        "team2": "Royal Challengers Bangalore",
        "date": "2025-05-29",
        "time": "19:30",
        "venue": "Rajiv Gandhi International Stadium, Hyderabad"
    },
    {
        "id": 75,
        "team1": "Delhi Capitals",
        "team2": "Gujarat Titans",
        "date": "2025-05-30",
        "time": "19:30",
        "venue": "Arun Jaitley Stadium, Delhi"
    }
]

# List of usernames
usernames = ["Anupam", "Akhil", "Abhishek", "Dinesh", "Prashant", "Shantanu"]

@app.route('/')
def index():
    logger.debug("Accessing index route")
    page = request.args.get('page', 1, type=int)
    per_page = 5
    total_pages = (len(fixtures) + per_page - 1) // per_page
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    current_fixtures = fixtures[start_idx:end_idx]
    
    return render_template('index.html', 
                         fixtures=current_fixtures,
                         current_page=page,
                         total_pages=total_pages,
                         usernames=usernames)

@app.route('/api/place_bet', methods=['POST'])
def place_bet():
    logger.debug("Received bet placement request")
    data = request.get_json()
    logger.debug(f"Received data: {data}")
    
    if not data:
        logger.error("No data received in request")
        return jsonify({'success': False, 'error': 'No data received'})
    
    required_fields = ['match', 'amount', 'team', 'username', 'opponent']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        logger.error(f"Missing required fields: {missing_fields}")
        return jsonify({'success': False, 'error': f'Missing required fields: {", ".join(missing_fields)}'})
    
    if not data['opponent']:
        logger.error("Opponent field is required")
        return jsonify({'success': False, 'error': 'Opponent field is required'})
    
    if data['username'] == data['opponent']:
        logger.error("User cannot bet against themselves")
        return jsonify({'success': False, 'error': 'You cannot bet against yourself'})
    
    try:
        amount = float(data['amount'])
        if amount <= 0:
            logger.error(f"Invalid amount: {amount}")
            return jsonify({'success': False, 'error': 'Amount must be greater than 0'})
    except ValueError:
        logger.error(f"Invalid amount format: {data['amount']}")
        return jsonify({'success': False, 'error': 'Invalid amount format'})
    
    try:
        logger.debug(f"Attempting to add bet: match={data['match']}, amount={amount}, team={data['team']}, username={data['username']}, opponent={data['opponent']}")
        success, bet_id = add_bet(
            match=data['match'],
            amount=amount,
            team=data['team'],
            username=data['username'],
            opponent=data['opponent']
        )
        
        if success:
            logger.info(f"Bet placed successfully with ID: {bet_id}")
            return jsonify({'success': True, 'id': bet_id})
        else:
            logger.error("Failed to place bet")
            return jsonify({'success': False, 'error': 'Failed to place bet'})
    except Exception as e:
        logger.error(f"Error placing bet: {str(e)}")
        return jsonify({'success': False, 'error': f'Error placing bet: {str(e)}'})

@app.route('/api/bets')
def get_bets():
    bets = get_all_bets()
    logger.debug(f"Returning {len(bets)} bets")
    return jsonify(bets)

if __name__ == '__main__':
    logger.info("Starting Flask application...")
    # Use environment variable for port with a default of 5000
    port = int(os.environ.get('PORT', 5000))
    # In production, host should be '0.0.0.0' to accept all incoming connections
    app.run(host='0.0.0.0', port=port, debug=False) 
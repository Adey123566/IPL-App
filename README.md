# IPL Betting App 🏏

A modern web application for managing friendly IPL betting among friends. Built with Flask and modern UI components.

## Features

- 🏆 View all IPL 2025 matches with details
- 🎯 Place bets on matches
- 👥 Select opponents for betting
- 💰 Track betting history
- 📱 Responsive design
- 🎨 Modern UI with IPL theme

## Tech Stack

- Backend: Python/Flask
- Frontend: HTML, CSS, JavaScript
- Database: SQLite
- UI Framework: Bootstrap 5
- Icons: Font Awesome

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ipl-betting-app.git
cd ipl-betting-app
```

2. Create a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Select your username from the dropdown
2. Choose an opponent
3. Select the team you want to bet on
4. Enter the bet amount
5. Click "Place Bet"

The betting history will automatically update to show your placed bet.

## Project Structure

```
ipl-betting-app/
├── app.py              # Main Flask application
├── database.py         # Database operations
├── requirements.txt    # Python dependencies
├── templates/         
│   └── index.html     # Main template
├── static/            
│   └── css/          
│       └── style.css  # Custom styles
└── README.md          # Documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- IPL for the inspiration
- Flask community for the excellent framework
- Bootstrap team for the UI components # IPL-App

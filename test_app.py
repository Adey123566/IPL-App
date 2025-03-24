from flask import Flask
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    logger.info('Homepage requested')
    return '<h1>Hello! IPL Betting App Test Page</h1>'

@app.route('/test')
def test():
    return 'Test route working!'

if __name__ == '__main__':
    try:
        logger.info('Starting Flask app on port 3000...')
        app.run(host='localhost', port=3000, debug=True)
    except Exception as e:
        logger.error(f'Error starting the app: {e}') 
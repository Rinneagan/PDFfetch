import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
SERPAPI_KEY = os.getenv('SERPAPI_KEY')
if not SERPAPI_KEY:
    raise ValueError("SERPAPI_KEY environment variable is not set. Please create a .env file with your API key.")

# Application Settings
DEFAULT_DOWNLOAD_DIR = os.path.join(os.path.expanduser('~'), 'Documents')
MAX_RETRIES = 3
TIMEOUT = 30  # seconds
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB
MAX_CONCURRENT_DOWNLOADS = 3
MAX_SEARCH_RESULTS = 50  # Maximum number of search results to return 
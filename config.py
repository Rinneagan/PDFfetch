import os
import sys
import dotenv

# Load environment variables from multiple possible .env locations with fallback and priorities:
# Priority (highest to lowest):
# 1. OS environment variables (pre-set)
# 2. User home profile directory (~/.pact/.env)
# 3. Executable directory (or script directory in dev)
# 4. Current working directory (.env)

pact_dir = os.path.join(os.path.expanduser("~"), ".pact")
user_env_path = os.path.join(pact_dir, ".env")

if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))
exe_env_path = os.path.join(exe_dir, ".env")

cwd_env_path = os.path.abspath(".env")

def read_env_keys(path: str) -> dict[str, str]:
    """Read key-value pairs from a .env file, ignoring empty values."""
    if os.path.exists(path):
        try:
            vals = dotenv.dotenv_values(path)
            return {k: v for k, v in vals.items() if v is not None and v.strip() != ""}
        except Exception:
            pass
    return {}

# Merge envs (lowest to highest priority, so later overrides earlier)
merged_env = {}
merged_env.update(read_env_keys(cwd_env_path))
merged_env.update(read_env_keys(exe_env_path))
merged_env.update(read_env_keys(user_env_path))

# Apply merged environment variables to os.environ
for k, v in merged_env.items():
    os.environ[k] = v

# API Configuration (System env has final priority)
SERPAPI_KEY = os.getenv('SERPAPI_KEY', '')

# Application Settings
DEFAULT_DOWNLOAD_DIR = os.path.join(os.path.expanduser('~'), 'Documents', 'Pact Downloads')
MAX_RETRIES = 3
TIMEOUT = 30  # seconds
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB
MAX_CONCURRENT_DOWNLOADS = 3
MAX_SEARCH_RESULTS = 50  # Maximum number of search results to return 
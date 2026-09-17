import sys
from pathlib import Path

# Ensure root directory is in sys.path so 'api' and other modules can be imported
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from app import app

# Vercel serverless WSGI/ASGI handler compatibility
handler = app

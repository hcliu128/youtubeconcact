import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

DOWNLOADS = 'downloads'
CAP_DIR = os.path.join(DOWNLOADS, 'captions')
VIDEO = os.path.join(DOWNLOADS, 'videos')


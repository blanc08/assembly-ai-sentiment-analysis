# importing os module for environment variables
import os

# importing necessary functions from dotenv library
from dotenv import load_dotenv

# loading variables from .env file
load_dotenv()

# accessing and printing value
API_KEY_ASSEMBLYAI = os.getenv("API_KEY_ASSEMBLYAI")

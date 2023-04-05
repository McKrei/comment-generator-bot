from dotenv import load_dotenv
import os

load_dotenv()

MODEL_GPT = "gpt-3.5-turbo"

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
OPEN_AI_API_TOKEN = os.environ.get("OPEN_AI_API_TOKEN")

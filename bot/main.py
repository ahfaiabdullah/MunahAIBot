import os
from dotenv import load_dotenv
from bot.telegram_bot import run_bot

load_dotenv()

if __name__ == "__main__":
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if token:
        run_bot(token)
    else:
        print("❗ TELEGRAM_BOT_TOKEN tak dijumpai. Pastikan .env lengkap.")
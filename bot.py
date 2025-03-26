from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()
BOTAPIKEY =  os.getenv("BOTAPIKEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Send a message with TWO buttons for different mini apps
    await update.message.reply_text(
        "🌟 Welcome! Choose an app:",
        reply_markup={
            "inline_keyboard": [
                # First row: Crypto Tracker
                [{
                    "text": "Krypto Prices 🪙",
                    "web_app": {"url": "https://krypto-kosi.onrender.com"}
                }],
                # Second row: Weather App
                [{
                    "text": "Weather forecast ?🌦️",
                    "web_app": {"url": "https://kosi-weather.onrender.com"}
                }],
                [{
                    "text": "Collaborative Drawing",
                    "web_app": {"url": "https://kolaborasi-kosi.onrender.com"}
                }],
                [{
                    "text": "Kosi's Portfolio",
                    "web_app": {"url": "https://kosisochukwu.onrender.com"}
                }]
            ]
        }
    )

# Add more commands like /help, /about, etc.
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Need help? Contact me!")

# Initialize the bot
application = Application.builder().token(BOTAPIKEY).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help))
application.run_polling()
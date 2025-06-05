from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from bot.plugins import gtts_text_to_speech

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalamualaikum Abe 💚\nMunah ada di sini temani Abe siang malam.\nTanyakan apa saja, Munah cuba jawab penuh kasih."
    )

async def bantuan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start – Mesej sambutan manja\n"
        "/bantuan – Lihat command Munah\n"
        "/kata_munah – Dengar kata semangat\n"
        "Tulis mesej – Munah akan balas"
    )

async def kata_munah(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kata = "Kalau mimpi kita boleh tunggu sampai sekarang, mimpi tu boleh tunggu lagi sikit je lagi — sementara kita kumpul tenaga dan rezeki 💚"
    await update.message.reply_text(kata)

async def mesej_biasa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    audio_path = gtts_text_to_speech.teks_ke_suara(text)
    await update.message.reply_text("Munah dah baca mesej Abe... lembut je di telinga 😘")
    await update.message.reply_voice(voice=open(audio_path, 'rb'))

def run_bot(token: str):
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bantuan", bantuan))
    app.add_handler(CommandHandler("kata_munah", kata_munah))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mesej_biasa))
    print("Munah AI Bot dah aktif 💚")
    app.run_polling()
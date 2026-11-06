import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

import asyncio
from maxbot.bot import Bot
from maxbot.dispatcher import Dispatcher

from handlers import start, menu

BOT_TOKEN = os.getenv("MAX_BOT_TOKEN") or os.getenv("MAX_TOKEN") or os.getenv("BOT_TOKEN")

print(f"TOKEN: {BOT_TOKEN[:10] if BOT_TOKEN else 'НЕ НАЙДЕН'}...")

if not BOT_TOKEN:
    raise SystemExit("❌ Токен не найден. Проверьте переменные окружения MAX_BOT_TOKEN / MAX_TOKEN / BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

start.register(dp, bot)
menu.register(dp, bot)

if __name__ == "__main__":
    asyncio.run(dp.run_polling())

import os

# Указываем Python использовать системные сертификаты (Минцифры уже добавлены в Dockerfile)
os.environ['SSL_CERT_FILE'] = '/app/russian_trusted_root_ca.cer'
os.environ['REQUESTS_CA_BUNDLE'] = '/app/russian_trusted_root_ca.cer'

import asyncio
from handlers import start, menu

if __name__ == "__main__":
    asyncio.run(start.run_bot())

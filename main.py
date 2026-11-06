import os

# Указываем Python использовать системные сертификаты (Минцифры уже добавлены в Dockerfile)
os.environ['SSL_CERT_FILE'] = '/etc/ssl/certs/ca-certificates.crt'
os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/certs/ca-certificates.crt'

import asyncio
from handlers import start, menu

if __name__ == "__main__":
    asyncio.run(start.run_bot())

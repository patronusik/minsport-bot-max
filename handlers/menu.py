import ssl
import aiohttp
import logging
import sys
import os

from config import (
    MAX_BOT_TOKEN,
    TEXT_WELCOME, TEXT_NOT_SUBSCRIBED,
    TEXT_INSTITUTIONS, TEXT_CALENDAR,
    TEXT_CAL_ASTRAKHANOCHKA, TEXT_CAL_VOLGAR, TEXT_CAL_DINAMO,
    TEXT_CAL_DINAMO_VK, TEXT_CAL_ASTRAKHAN,
    TEXT_ATHLETES, TEXT_RANKS_WHO,
    TEXT_GTO_MENU, TEXT_GTO_HOW, TEXT_GTO_CENTERS,
    TEXT_TAX_MENU, TEXT_TAX_SPORT,
    TEXT_CONTACTS
)
from keyboards import (
    main_menu_kb, back_to_menu_kb, subscribe_kb,
    institutions_kb, calendar_kb, back_to_calendar_kb,
    athletes_kb, ranks_kb, back_to_ranks_kb,
    gto_kb, back_to_gto_kb,
    tax_kb, tax_sport_kb,
    federations_kb,
    inst_kaspiy_kb, inst_volgar_kb, inst_zarya_kb,
    inst_zvezdny_kb, inst_winter_kb,
)
from handlers.start import is_user_subscribed

# --- ЛОГГЕР ---
logger = logging.getLogger("menu")
logger.setLevel(logging.DEBUG)
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(asctime)s [MENU] %(message)s"))
    logger.addHandler(handler)


def log(msg):
    print(msg, flush=True)
    logger.info(msg)


def check_ssl_paths():
    """Проверяет, какие пути сертификатов использует Python."""
    log("=" * 60)
    log("SSL CERTIFICATE PATHS CHECK")

    # 1. Переменные окружения
    ssl_cert_file = os.environ.get("SSL_CERT_FILE", "<not set>")
    requests_ca_bundle = os.environ.get("REQUESTS_CA_BUNDLE", "<not set>")
    log(f"ENV SSL_CERT_FILE = {ssl_cert_file}")
    log(f"ENV REQUESTS_CA_BUNDLE = {requests_ca_bundle}")

    # 2. Пути по умолчанию из ssl модуля
    try:
        paths = ssl.get_default_verify_paths()
        log(f"ssl.get_default_verify_paths().cafile = {paths.cafile}")
        log(f"ssl.get_default_verify_paths().capath = {paths.capath}")
        log(f"ssl.get_default_verify_paths().openssl_cafile_env = {paths.openssl_cafile_env}")
    except Exception as e:
        log(f"ssl.get_default_verify_paths() FAILED: {e}")

    # 3. Проверка, существует ли системный файл
    system_ca = "/etc/ssl/certs/ca-certificates.crt"
    exists = os.path.exists(system_ca)
    log(f"System CA file {system_ca} exists = {exists}")
    if exists:
        size = os.path.getsize(system_ca)
        log(f"System CA file size = {size} bytes")

    # 4. Проверка certifi
    try:
        import certifi
        certifi_path = certifi.where()
        log(f"certifi.where() = {certifi_path}")
        certifi_exists = os.path.exists(certifi_path)
        log(f"certifi bundle exists = {certifi_exists}")
    except Exception as e:
        log(f"certifi check FAILED: {e}")

    log("=" * 60)


def _kb_to_attachments(keyboard):
    if keyboard is None:
        return None
    buttons = []
    for row in keyboard.inline_keyboard:
        btn_row = []
        for btn in row:
            if getattr(btn, "url", None):
                b = {"type": "link", "text": btn.text, "url": btn.url}
            else:
                b = {"type": "callback", "text": btn.text, "payload": getattr(btn, "callback_data", "")}
            btn_row.append(b)
        buttons.append(btn_row)
    return [{"type": "inline_keyboard", "payload": {"buttons": buttons}}]


async def _edit_message_http(message_id, text, keyboard):
    url = f"https://platform-api2.max.ru/messages?message_id={message_id}"
    headers = {
        "Authorization": MAX_BOT_TOKEN,
        "Content-Type": "application/json"
    }
    body = {"text": text, "format": "markdown"}
    att = _kb_to_attachments(keyboard)
    if att:
        body["attachments"] = att

    # Пробуем создать SSL-контекст с системным файлом
    system_ca = "/etc/ssl/certs/ca-certificates.crt"
    ssl_context = None
    try:
        if os.path.exists(system_ca):
            ssl_context = ssl.create_default_context(cafile=system_ca)
            log(f"SSL context created with cafile={system_ca}")
        else:
            ssl_context = ssl.create_default_context()
            log("SSL context created with default paths (system file not found)")
    except Exception as e:
        log(f"SSL context creation FAILED: {e}")
        ssl_context = None

    log(f"EDIT REQ: url={url}")
    log(f"EDIT REQ body: {str(body)[:500]}")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, headers=headers, json=body, ssl=ssl_context) as resp:
                txt = await resp.text()
                log(f"EDIT RESP: status={resp.status}, body={txt[:500]}")
                return resp.status == 200
    except Exception as e:
        log(f"EDIT EXCEPTION: {type(e).__name__}: {e}")
        return False


def register(dp, bot):
    # При запуске проверяем пути сертификатов
    check_ssl_paths()

    @dp.callback()
    async def on_callback(cb):
        log("=" * 70)
        log("CALLBACK HANDLER STARTED")

        # --- 1. ANSWER CALLBACK ---
        callback_id = getattr(cb, "callback_id", None)
        if callback_id is None and hasattr(cb, "data") and isinstance(cb.data, dict):
            callback_id = cb.data.get("callback_id")
        log(f"1. callback_id = {callback_id}")

        if callback_id:
            try:
                await bot.answer_callback(callback_id=callback_id, notification="")
                log("1. ANSWER_CALLBACK OK")
            except Exception as e:
                log(f"1. ANSWER_CALLBACK FAILED: {e}")
        else:
            log("1. ANSWER_CALLBACK SKIPPED: callback_id not found")

        # --- 2. USER ID ---
        user_id = None
        if hasattr(cb, "user") and cb.user is not None:
            user_id = getattr(cb.user, "id", None) or (
                cb.user.get("user_id") if isinstance(cb.user, dict) else None
            )
        if user_id is None:
            user_id = getattr(cb, "user_id", None)
        log(f"2. user_id = {user_id}")

        # --- 3. MESSAGE ID ---
        message_id = None
        if hasattr(cb, "message") and cb.message is not None:
            m = cb.message
            if isinstance(m, dict):
                message_id = m.get("mid") or m.get("id")
            else:
                message_id = getattr(m, "mid", None) or getattr(m, "id", None)
        if message_id is None and hasattr(cb, "message_id"):
            message_id = cb.message_id
        log(f"3. message_id = {message_id}")

        payload = cb.payload
        log(f"4. payload = {payload}")

        # --- 5. ПРОВЕРКА ПОДПИСКИ ---
        subscribed = await is_user_subscribed(user_id)
        log(f"5. subscribed = {subscribed}")
        if not subscribed and payload not in ("check_sub", "back_to_menu"):
            await bot.send_message(
                user_id=user_id,
                text=TEXT_NOT_SUBSCRIBED,
                reply_markup=subscribe_kb
            )
            log("5. SENT NOT_SUBSCRIBED message")
            return

        # --- 6. ВЫБОР ТЕКСТА И КЛАВИАТУРЫ ---
        text = None
        keyboard = None

        if payload == "check_sub":
            text = TEXT_WELCOME
            keyboard = main_menu_kb
        elif payload == "back_to_menu":
            text = TEXT_WELCOME
            keyboard = main_menu_kb
        elif payload == "institutions":
            text, keyboard = TEXT_INSTITUTIONS, institutions_kb
        elif payload == "inst_kaspiy":
            text, keyboard = "🏛 ГАУ АО РЦСА «Каспий»\n\nВыберите подраздел:", inst_kaspiy_kb
        elif payload == "inst_volgar":
            text, keyboard = "🏛 ГАУ АО РЦСП «Волгарь»\n\nВыберите подраздел:", inst_volgar_kb
        elif payload == "inst_zarya":
            text, keyboard = "🏛 ГАУ АО РЦСП «Заря Каспия»\n\nВыберите подраздел:", inst_zarya_kb
        elif payload == "inst_zvezdny":
            text, keyboard = "🏛 ГАУ АО РЦСП «Звёздный»\n\nВыберите подраздел:", inst_zvezdny_kb
        elif payload == "inst_winter":
            text, keyboard = "🏛 ГАУ АО «Центр зимних видов спорта»\n\nВыберите подраздел:", inst_winter_kb
        elif payload == "calendar":
            text, keyboard = TEXT_CALENDAR, calendar_kb
        elif payload == "cal_astrakhanochka":
            text, keyboard = TEXT_CAL_ASTRAKHANOCHKA, back_to_calendar_kb
        elif payload == "cal_volgar":
            text, keyboard = TEXT_CAL_VOLGAR, back_to_calendar_kb
        elif payload == "cal_dinamo":
            text, keyboard = TEXT_CAL_DINAMO, back_to_calendar_kb
        elif payload == "cal_dinamo_vk":
            text, keyboard = TEXT_CAL_DINAMO_VK, back_to_calendar_kb
        elif payload == "cal_astrakhan":
            text, keyboard = TEXT_CAL_ASTRAKHAN, back_to_calendar_kb
        elif payload == "athletes":
            text, keyboard = TEXT_ATHLETES, athletes_kb
        elif payload == "ranks":
            text, keyboard = "🏅 **Присвоение спортивных разрядов и званий**\n\nВыберите подраздел:", ranks_kb
        elif payload == "ranks_who":
            text, keyboard = TEXT_RANKS_WHO, back_to_ranks_kb
        elif payload == "gto_menu":
            text, keyboard = TEXT_GTO_MENU, gto_kb
        elif payload == "gto_how":
            text, keyboard = TEXT_GTO_HOW, back_to_gto_kb
        elif payload == "gto_centers":
            text, keyboard = TEXT_GTO_CENTERS, back_to_gto_kb
        elif payload == "tax_menu":
            text, keyboard = TEXT_TAX_MENU, tax_kb
        elif payload == "tax_sport":
            text, keyboard = TEXT_TAX_SPORT, tax_sport_kb
        elif payload == "federations":
            text, keyboard = "🤝 **Федерациям, НКО и частным клубам**\n\nВыберите раздел:", federations_kb
        elif payload == "contacts":
            text, keyboard = TEXT_CONTACTS, back_to_menu_kb
        else:
            log(f"6. UNHANDLED PAYLOAD: {payload}")
            return

        log(f"6. text length = {len(text) if text else 0}")
        log(f"6. keyboard = {keyboard is not None}")

        # --- 7. РЕДАКТИРОВАНИЕ ИЛИ ОТПРАВКА ---
        if message_id:
            log("7. Trying to EDIT message via HTTP...")
            ok = await _edit_message_http(message_id, text, keyboard)
            if ok:
                log("7. EDIT SUCCESS")
                return
            log("7. EDIT FAILED, fallback to send_message")
        else:
            log("7. No message_id, sending new message")

        try:
            await bot.send_message(
                user_id=user_id,
                text=text,
                reply_markup=keyboard,
                format="markdown"
            )
            log("7. SEND_MESSAGE OK")
        except Exception as e:
            log(f"7. SEND_MESSAGE FAILED: {type(e).__name__}: {e}")

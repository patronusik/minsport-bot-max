import ssl
import certifi
import aiohttp
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


def _kb_to_attachments(keyboard):
    """Преобразует InlineKeyboardMarkup umaxbot в формат attachments MAX API."""
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
    """Редактирует сообщение напрямую через API MAX (токен в заголовке, SSL через certifi)."""
    url = f"https://platform-api2.max.ru/messages?message_id={message_id}"
    headers = {
        "Authorization": MAX_BOT_TOKEN,
        "Content-Type": "application/json"
    }
    body = {"text": text, "format": "markdown"}
    att = _kb_to_attachments(keyboard)
    if att:
        body["attachments"] = att

    # Явный SSL-контекст с сертификатами certifi (в контейнере нет системных корней)
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    print(f"EDIT REQ: url={url}, body_keys={list(body.keys())}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, headers=headers, json=body, ssl=ssl_context) as resp:
                txt = await resp.text()
                print(f"EDIT RESP: status={resp.status}, body={txt[:300]}")
                return resp.status == 200
    except Exception as e:
        print(f"EDIT EXCEPTION: {e}")
        return False


def register(dp, bot):

    @dp.callback()
    async def on_callback(cb):
        print("=" * 60)
        print("RAW CALLBACK RECEIVED")

        # --- ANSWER_CALLBACK ---
        callback_id = getattr(cb, "callback_id", None)
        if callback_id is None and hasattr(cb, "data") and isinstance(cb.data, dict):
            callback_id = cb.data.get("callback_id")
        print(f"RESOLVED callback_id = {callback_id}")

        if callback_id:
            try:
                await bot.answer_callback(callback_id=callback_id, notification="")
                print("ANSWER_CALLBACK OK")
            except Exception as e:
                print(f"ANSWER_CALLBACK FAILED: {e}")
        else:
            print("ANSWER_CALLBACK SKIPPED: callback_id not found")

        # --- USER_ID ---
        user_id = None
        if hasattr(cb, "user") and cb.user is not None:
            user_id = getattr(cb.user, "id", None) or (
                cb.user.get("user_id") if isinstance(cb.user, dict) else None
            )
        if user_id is None:
            user_id = getattr(cb, "user_id", None)
        print(f"RESOLVED user_id = {user_id}")

        # --- MESSAGE_ID ---
        message_id = None
        if hasattr(cb, "message") and cb.message is not None:
            m = cb.message
            if isinstance(m, dict):
                message_id = m.get("mid") or m.get("id")
            else:
                message_id = getattr(m, "mid", None) or getattr(m, "id", None)
        if message_id is None and hasattr(cb, "message_id"):
            message_id = cb.message_id
        print(f"RESOLVED message_id = {message_id}")

        payload = cb.payload
        print(f"PAYLOAD = {payload}")
        print("=" * 60)

        async def show(text, keyboard):
            print(f"SHOW CALLED: message_id={message_id}")
            if message_id:
                ok = await _edit_message_http(message_id, text, keyboard)
                if ok:
                    print("SHOW: edit success")
                    return
                print("SHOW: edit failed, fallback to send")
            print("SHOW: sending new message")
            await bot.send_message(
                user_id=user_id,
                text=text,
                reply_markup=keyboard,
                format="markdown"
            )

        # --- ПОДПИСКА ---
        if payload == "check_sub":
            subscribed = await is_user_subscribed(user_id)
            print(f"SUBSCRIBED = {subscribed}")
            if subscribed:
                await show(TEXT_WELCOME, main_menu_kb)
            else:
                await bot.send_message(
                    user_id=user_id,
                    text=TEXT_NOT_SUBSCRIBED,
                    reply_markup=subscribe_kb
                )
            return

        if payload == "back_to_menu":
            await show(TEXT_WELCOME, main_menu_kb)
            return

        subscribed = await is_user_subscribed(user_id)
        print(f"SUBSCRIBED = {subscribed}")
        if not subscribed:
            await bot.send_message(
                user_id=user_id,
                text=TEXT_NOT_SUBSCRIBED,
                reply_markup=subscribe_kb
            )
            return

        # --- РАЗДЕЛ 1: УЧРЕЖДЕНИЯ ---
        if payload == "institutions":
            await show(TEXT_INSTITUTIONS, institutions_kb)
        elif payload == "inst_kaspiy":
            await show("🏛 ГАУ АО РЦСА «Каспий»\n\nВыберите подраздел:", inst_kaspiy_kb)
        elif payload == "inst_volgar":
            await show("🏛 ГАУ АО РЦСП «Волгарь»\n\nВыберите подраздел:", inst_volgar_kb)
        elif payload == "inst_zarya":
            await show("🏛 ГАУ АО РЦСП «Заря Каспия»\n\nВыберите подраздел:", inst_zarya_kb)
        elif payload == "inst_zvezdny":
            await show("🏛 ГАУ АО РЦСП «Звёздный»\n\nВыберите подраздел:", inst_zvezdny_kb)
        elif payload == "inst_winter":
            await show("🏛 ГАУ АО «Центр зимних видов спорта»\n\nВыберите подраздел:", inst_winter_kb)

        # --- РАЗДЕЛ 2: КАЛЕНДАРЬ ---
        elif payload == "calendar":
            await show(TEXT_CALENDAR, calendar_kb)
        elif payload == "cal_astrakhanochka":
            await show(TEXT_CAL_ASTRAKHANOCHKA, back_to_calendar_kb)
        elif payload == "cal_volgar":
            await show(TEXT_CAL_VOLGAR, back_to_calendar_kb)
        elif payload == "cal_dinamo":
            await show(TEXT_CAL_DINAMO, back_to_calendar_kb)
        elif payload == "cal_dinamo_vk":
            await show(TEXT_CAL_DINAMO_VK, back_to_calendar_kb)
        elif payload == "cal_astrakhan":
            await show(TEXT_CAL_ASTRAKHAN, back_to_calendar_kb)

        # --- РАЗДЕЛ 3: СПОРТСМЕНАМ ---
        elif payload == "athletes":
            await show(TEXT_ATHLETES, athletes_kb)
        elif payload == "ranks":
            await show("🏅 **Присвоение спортивных разрядов и званий**\n\nВыберите подраздел:", ranks_kb)
        elif payload == "ranks_who":
            await show(TEXT_RANKS_WHO, back_to_ranks_kb)

        # --- РАЗДЕЛ 4: ГТО ---
        elif payload == "gto_menu":
            await show(TEXT_GTO_MENU, gto_kb)
        elif payload == "gto_how":
            await show(TEXT_GTO_HOW, back_to_gto_kb)
        elif payload == "gto_centers":
            await show(TEXT_GTO_CENTERS, back_to_gto_kb)

        # --- РАЗДЕЛ 5: НАЛОГОВЫЙ ВЫЧЕТ ---
        elif payload == "tax_menu":
            await show(TEXT_TAX_MENU, tax_kb)
        elif payload == "tax_sport":
            await show(TEXT_TAX_SPORT, tax_sport_kb)

        # --- РАЗДЕЛ 8: ФЕДЕРАЦИЯМ ---
        elif payload == "federations":
            await show("🤝 **Федерациям, НКО и частным клубам**\n\nВыберите раздел:", federations_kb)

        # --- РАЗДЕЛ 9: КОНТАКТЫ ---
        elif payload == "contacts":
            await show(TEXT_CONTACTS, back_to_menu_kb)

        else:
            print(f"UNHANDLED PAYLOAD: {payload}")

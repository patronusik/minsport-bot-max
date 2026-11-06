from handlers.start import send_message, is_user_subscribed
from config import (
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

async def handle_menu(payload, user_id, message_id):
    # Проверка подписки (временно отключена, чтобы меню работало)
    # subscribed = await is_user_subscribed(user_id)
    # if not subscribed and payload not in ("check_sub", "back_to_menu"):
    #     await send_message(user_id, TEXT_NOT_SUBSCRIBED, keyboard=subscribe_kb)
    #     return

    text = None
    keyboard = None

    if payload == "check_sub":
        text, keyboard = TEXT_WELCOME, main_menu_kb
    elif payload == "back_to_menu":
        text, keyboard = TEXT_WELCOME, main_menu_kb
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
        print(f"UNHANDLED: {payload}", flush=True)
        return

    # Отправляем с редактированием (если есть message_id)
    await send_message(user_id, text, keyboard=keyboard, message_id=message_id)

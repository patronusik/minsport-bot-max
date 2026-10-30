from maxbot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_URL, SITE_URL

# --- ПРОВЕРКА ПОДПИСКИ ---
subscribe_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📢 Открыть канал", url=CHANNEL_URL)],
    [InlineKeyboardButton(text="✅ Я подписан", callback_data="check_sub")]
])

# --- ГЛАВНОЕ МЕНЮ ---
main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏛 Гос учреждения министерства", callback_data="institutions")],
    [InlineKeyboardButton(text="📅 Календарь профессиональных команд", callback_data="calendar")],
    [InlineKeyboardButton(text="🏅 Спортсменам", callback_data="athletes")],
    [InlineKeyboardButton(text="🏃 Комплекс ГТО", callback_data="gto_menu")],
    [InlineKeyboardButton(text="💰 Налоговый вычет", callback_data="tax_menu")],
    [InlineKeyboardButton(text="🏆 Земский тренер", url="https://minsport.astrobl.ru/activity/zemskii-trener")],
    [InlineKeyboardButton(text="📋 Список федераций Астраханской области", url="https://minsport.astrobl.ru/docs/document-document-16g3-4e0a3-8i0a-8i5")],
    [InlineKeyboardButton(text="🤝 Федерациям, НКО и частным клубам", callback_data="federations")],
    [InlineKeyboardButton(text="📞 Контактная информация", callback_data="contacts")],
])

back_to_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- РАЗДЕЛ 1: УЧРЕЖДЕНИЯ ---
# ВНИМАНИЕ: замени URL-заглушки на реальные ссылки ботов учреждений
institutions_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ГКУ АО РЦСП", url="https://max.ru/rcspastroblbot")],
    [InlineKeyboardButton(text="ГБУ ДО АО СШОР им. Кузнецова", url="https://max.ru/shorkuznecov_bot")],
    [InlineKeyboardButton(text="ГБУ ДО АО СШОР им. Скокова", url="https://max.ru/skokovinfobot")],
    [InlineKeyboardButton(text="ГКУ ДО АО ОСШ", url="https://max.ru/oblastnayasportshkola30_bot")],
    [InlineKeyboardButton(text="ГБУ ДО АО СШОР 1", url="https://max.ru/shor1_30_bot")],
    [InlineKeyboardButton(text="ГБУ ДО АО СШОР им. Тихомировой", url="https://max.ru/grace30_bot")],
    [InlineKeyboardButton(text="ГКУ ДО АО СШОР им. Тихонова", url="https://max.ru/rowing30_bot")],
    [InlineKeyboardButton(text="ГКУ ДО АО СШОР им. Гладченко", url="https://max.ru/shor_gladchenko_bot")],
    [InlineKeyboardButton(text="ГАУ ДО АО СШОР им. Гладилина", url="https://max.ru/ССЫЛКА_НА_БОТА")],
    [InlineKeyboardButton(text="ГАУ АО РЦСП «Каспий»", callback_data="inst_kaspiy")],
    [InlineKeyboardButton(text="ГАУ АО РЦСП «Волгарь»", callback_data="inst_volgar")],
    [InlineKeyboardButton(text="ГАУ АО РЦСП «Заря Каспия»", callback_data="inst_zarya")],
    [InlineKeyboardButton(text="ГАУ АО РЦСП «Звёздный»", callback_data="inst_zvezdny")],
    [InlineKeyboardButton(text="ГАУ АО «ЦРСИ»", url="https://max.ru/newpokolenie30_maxbot")],
    [InlineKeyboardButton(text="ГАУ АО «Центр зимних видов спорта»", callback_data="inst_winter")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- РАЗДЕЛ 2: КАЛЕНДАРЬ ---
calendar_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ГК «Астраханочка»", callback_data="cal_astrakhanochka")],
    [InlineKeyboardButton(text="ФК «Волгарь»", callback_data="cal_volgar")],
    [InlineKeyboardButton(text="ГК «Динамо»", callback_data="cal_dinamo")],
    [InlineKeyboardButton(text="ВК «Динамо-СШОР»", callback_data="cal_dinamo_vk")],
    [InlineKeyboardButton(text="СК «Астрахань»", callback_data="cal_astrakhan")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

back_to_calendar_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к календарю", callback_data="calendar")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- РАЗДЕЛ 3: СПОРТСМЕНАМ ---
athletes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Присвоение спортивных разрядов и званий", callback_data="ranks")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

ranks_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кто может подать?", callback_data="ranks_who")],
    [InlineKeyboardButton(text="Порядок подачи", url="https://minsport.astrobl.ru/documents/prisvoenie-sportivnyx-razryadov")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="athletes")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

back_to_ranks_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="ranks")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- РАЗДЕЛ 4: ГТО ---
gto_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Нормативы ГТО для мужчин и женщин", url="https://www.gto.ru/normativy/")],
    [InlineKeyboardButton(text="Как выполнить нормы ГТО", callback_data="gto_how")],
    [InlineKeyboardButton(text="Центры тестирования", callback_data="gto_centers")],
    [InlineKeyboardButton(text="Вход в личный кабинет", url="https://auth.gto.gov.ru/")],
    [InlineKeyboardButton(text="Приказы о награждении золотым знаком", url="https://www.gto.ru/dokumenty/prikazy-o-nagrazhdenii/")],
    [InlineKeyboardButton(text="Приказы о награждении серебряным и бронзовым знаком", url="https://newpokolenie.ru/приказы")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

back_to_gto_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к ГТО", callback_data="gto_menu")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- РАЗДЕЛ 5: НАЛОГОВЫЙ ВЫЧЕТ ---
tax_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Налоговый вычет за ГТО", url="https://minsport.astrobl.ru/news/s-2025-goda-mozhno-poluchit-nalogovyy-vychet-za-sdachu-norm-gto")],
    [InlineKeyboardButton(text="Налоговый вычет за занятия ФКиС", callback_data="tax_sport")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

back_to_tax_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="tax_menu")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

tax_sport_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Шаблоны заявлений и согласий", url="https://minsport.astrobl.ru/o-nalogovom-vycete-za-zaniatiia-sportom/sablony-zaiavlenii-i-soglasii")],
    [InlineKeyboardButton(text="Реестр организаций", url="https://minsport.gov.ru/activities/o-nalogovom-vychete-za-zanyatiya-sportom/")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="tax_menu")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- РАЗДЕЛ 8: ФЕДЕРАЦИЯМ ---
federations_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Государственная аккредитация", url="https://minsport.astrobl.ru/docs/document-86168idb313b30")],
    [InlineKeyboardButton(text="Лицензия на дополнительное образование", url="https://minsport.astrobl.ru/documents/akkreditaciya-federacii/poluchenie-licenzii-na-dopolnitelnoe-obrazovanie")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- ПОДМЕНЮ УЧРЕЖДЕНИЙ (где два подраздела) ---
inst_kaspiy_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Бот учреждения", url="https://max.ru/kaspiy30_bot")],
    [InlineKeyboardButton(text="Авангард", url="https://max.ru/ССЫЛКА_НА_АВАНГАРД")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="institutions")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

inst_volgar_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Бот АНО «Волгарь»", url="https://max.ru/ССЫЛКА_НА_БОТА")],
    [InlineKeyboardButton(text="ГАУ АО РЦСП «Волгарь»", url="https://max.ru/ССЫЛКА_НА_БОТА")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="institutions")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

inst_zarya_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Бот ГАУ АО РЦСП «Заря Каспия» (платные услуги)", url="https://max.ru/zaryakaspiya_bot")],
    [InlineKeyboardButton(text="Команда «Динамо»", url="https://max.ru/ССЫЛКА_НА_ДИНАМО")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="institutions")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

inst_zvezdny_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Бот СК «Звёздный» (платные услуги)", url="https://max.ru/ССЫЛКА_НА_БОТА")],
    [InlineKeyboardButton(text="ГК «Астраханочка»", url="https://max.ru/ССЫЛКА_НА_АСТРАХАНОЧКУ")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="institutions")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

inst_winter_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Бот учреждения", url="https://max.ru/gau_ao_czvs_bot")],
    [InlineKeyboardButton(text="Бот «Миланкор»", url="https://max.ru/ССЫЛКА_НА_БОТА")],
    [InlineKeyboardButton(text="Бот «Ястребов»", url="https://max.ru/ССЫЛКА_НА_БОТА")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="institutions")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

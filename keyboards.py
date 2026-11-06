# Клавиатуры в формате MAX API:
# [{"type": "callback", "text": "...", "payload": "..."}]
# [{"type": "link", "text": "...", "url": "..."}]

subscribe_kb = [
    [{"type": "link", "text": "📢 Открыть канал", "url": "https://max.ru/minsport30"}],
    [{"type": "callback", "text": "✅ Я подписан", "payload": "check_sub"}]
]

main_menu_kb = [
    [{"type": "callback", "text": "🏛 Гос учреждения министерства", "payload": "institutions"}],
    [{"type": "callback", "text": "📅 Календарь проф команд", "payload": "calendar"}],
    [{"type": "callback", "text": "🏅 Спортсменам", "payload": "athletes"}],
    [{"type": "callback", "text": "🏃 Комплекс ГТО", "payload": "gto_menu"}],
    [{"type": "callback", "text": "💰 Налоговый вычет", "payload": "tax_menu"}],
    [{"type": "link", "text": "🏆 Земский тренер", "url": "https://minsport.astrobl.ru/activity/zemskii-trener"}],
    [{"type": "link", "text": "📋 Список федераций АО", "url": "https://minsport.astrobl.ru/docs/document-document-16g3-4e0a3-8i0a-8i5"}],
    [{"type": "callback", "text": "🤝 Федерациям, НКО и ЧК", "payload": "federations"}],
    [{"type": "callback", "text": "📞 Контактная информация", "payload": "contacts"}],
]

back_to_menu_kb = [
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}]
]

# --- РАЗДЕЛ 1: УЧРЕЖДЕНИЯ ---
institutions_kb = [
    [{"type": "link", "text": "ГКУ АО РЦСП", "url": "https://max.ru/rcspastroblbot"}],
    [{"type": "link", "text": "ГБУ ДО АО СШОР им. Кузнецова", "url": "https://max.ru/shorkuznecov_bot"}],
    [{"type": "link", "text": "ГБУ ДО АО СШОР им. Скокова", "url": "https://max.ru/skokovinfobot"}],
    [{"type": "link", "text": "ГКУ ДО АО ОСШ", "url": "https://max.ru/oblastnayasportshkola30_bot"}],
    [{"type": "link", "text": "ГБУ ДО АО СШОР 1", "url": "https://max.ru/shor1_30_bot"}],
    [{"type": "link", "text": "ГБУ ДО АО СШОР им. Тихомировой", "url": "https://max.ru/grace30_bot"}],
    [{"type": "link", "text": "ГКУ ДО АО СШОР им. Тихонова", "url": "https://max.ru/rowing30_bot"}],
    [{"type": "link", "text": "ГКУ ДО АО СШОР им. Гладченко", "url": "https://max.ru/shor_gladchenko_bot"}],
    [{"type": "link", "text": "ГАУ ДО АО СШОР им. Гладилина", "url": "https://max.ru/shorvodnoepolobot"}],
    [{"type": "callback", "text": "ГАУ АО РЦСП «Каспий»", "payload": "inst_kaspiy"}],
    [{"type": "callback", "text": "ГАУ АО РЦСП «Волгарь»", "payload": "inst_volgar"}],
    [{"type": "callback", "text": "ГАУ АО РЦСП «Заря Каспия»", "payload": "inst_zarya"}],
    [{"type": "callback", "text": "ГАУ АО РЦСП «Звёздный»", "payload": "inst_zvezdny"}],
    [{"type": "link", "text": "ГАУ АО «ЦРСИ»", "url": "https://max.ru/newpokolenie30_maxbot"}],
    [{"type": "callback", "text": "ГАУ АО «Центр зимних видов спорта»", "payload": "inst_winter"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

# --- РАЗДЕЛ 2: КАЛЕНДАРЬ ---
calendar_kb = [
    [{"type": "callback", "text": "🤾 ГК «Астраханочка»", "payload": "cal_astrakhanochka"}],
    [{"type": "callback", "text": "⚽ ФК «Волгарь»", "payload": "cal_volgar"}],
    [{"type": "callback", "text": "🤾 ГК «Динамо»", "payload": "cal_dinamo"}],
    [{"type": "callback", "text": "🤽 ВК «Динамо-СШОР»", "payload": "cal_dinamo_vk"}],
    [{"type": "callback", "text": "⚽ СК «Астрахань»", "payload": "cal_astrakhan"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

back_to_calendar_kb = [
    [{"type": "callback", "text": "⬅️ Назад к календарю", "payload": "calendar"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

# --- РАЗДЕЛ 3: СПОРТСМЕНАМ ---
athletes_kb = [
    [{"type": "callback", "text": "Присвоение спортивных разрядов и званий", "payload": "ranks"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

ranks_kb = [
    [{"type": "callback", "text": "Кто может подать?", "payload": "ranks_who"}],
    [{"type": "link", "text": "Порядок подачи", "url": "https://minsport.astrobl.ru/documents/prisvoenie-sportivnyx-razryadov"}],
    [{"type": "callback", "text": "⬅️ Назад", "payload": "athletes"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

back_to_ranks_kb = [
    [{"type": "callback", "text": "⬅️ Назад", "payload": "ranks"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

# --- РАЗДЕЛ 4: ГТО ---
gto_kb = [
    [{"type": "link", "text": "Нормативы ГТО для мужчин и женщин", "url": "https://www.gto.ru/normativy/"}],
    [{"type": "callback", "text": "Как выполнить нормы ГТО", "payload": "gto_how"}],
    [{"type": "callback", "text": "Центры тестирования", "payload": "gto_centers"}],
    [{"type": "link", "text": "Вход в личный кабинет", "url": "https://auth.gto.gov.ru/"}],
    [{"type": "link", "text": "Приказы о награждении золотым знаком", "url": "https://www.gto.ru/dokumenty/prikazy-o-nagrazhdenii/"}],
    [{"type": "link", "text": "Приказы о награждении серебряным и бронзовым знаком", "url": "https://newpokolenie.ru/приказы"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

back_to_gto_kb = [
    [{"type": "callback", "text": "⬅️ Назад к ГТО", "payload": "gto_menu"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

# --- РАЗДЕЛ 5: НАЛОГОВЫЙ ВЫЧЕТ ---
tax_kb = [
    [{"type": "link", "text": "Налоговый вычет за ГТО", "url": "https://minsport.astrobl.ru/news/s-2025-goda-mozhno-poluchit-nalogovyy-vychet-za-sdachu-norm-gto"}],
    [{"type": "callback", "text": "Налоговый вычет за занятия ФКиС", "payload": "tax_sport"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

back_to_tax_kb = [
    [{"type": "callback", "text": "⬅️ Назад", "payload": "tax_menu"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

tax_sport_kb = [
    [{"type": "link", "text": "Шаблоны заявлений и согласий", "url": "https://minsport.astrobl.ru/o-nalogovom-vycete-za-zaniatiia-sportom/sablony-zaiavlenii-i-soglasii"}],
    [{"type": "link", "text": "Реестр организаций", "url": "https://minsport.gov.ru/activities/o-nalogovom-vychete-za-zanyatiya-sportom/"}],
    [{"type": "callback", "text": "⬅️ Назад", "payload": "tax_menu"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

# --- РАЗДЕЛ 8: ФЕДЕРАЦИЯМ ---
federations_kb = [
    [{"type": "link", "text": "Государственная аккредитация", "url": "https://minsport.astrobl.ru/docs/document-86168idb313b30"}],
    [{"type": "link", "text": "Лицензия на дополнительное образование", "url": "https://minsport.astrobl.ru/documents/akkreditaciya-federacii/poluchenie-licenzii-na-dopolnitelnoe-obrazovanie"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

# --- ПОДМЕНЮ УЧРЕЖДЕНИЙ ---
inst_kaspiy_kb = [
    [{"type": "link", "text": "Бот учреждения", "url": "https://max.ru/kaspiy30_bot"}],
    [{"type": "link", "text": "Авангард", "url": "https://max.ru/ССЫЛКА_НА_АВАНГАРД"}],
    [{"type": "callback", "text": "⬅️ Назад", "payload": "institutions"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

inst_volgar_kb = [
    [{"type": "link", "text": "Бот АНО «Волгарь»", "url": "https://max.ru/ССЫЛКА_НА_БОТА"}],
    [{"type": "link", "text": "ГАУ АО РЦСП «Волгарь»", "url": "https://max.ru/ССЫЛКА_НА_БОТА"}],
    [{"type": "callback", "text": "⬅️ Назад", "payload": "institutions"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

inst_zarya_kb = [
    [{"type": "link", "text": "Бот ГАУ АО РЦСП «Заря Каспия» (платные услуги)", "url": "https://max.ru/zaryakaspiya30_bot"}],
    [{"type": "link", "text": "Команда «Динамо»", "url": "https://max.ru/ССЫЛКА_НА_ДИНАМО"}],
    [{"type": "callback", "text": "⬅️ Назад", "payload": "institutions"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

inst_zvezdny_kb = [
    [{"type": "link", "text": "Бот СК «Звёздный» (платные услуги)", "url": "https://max.ru/ССЫЛКА_НА_БОТА"}],
    [{"type": "link", "text": "ГК «Астраханочка»", "url": "https://max.ru/ССЫЛКА_НА_АСТРАХАНОЧКУ"}],
    [{"type": "callback", "text": "⬅️ Назад", "payload": "institutions"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

inst_winter_kb = [
    [{"type": "link", "text": "Бот учреждения", "url": "https://max.ru/gau_ao_czvs_bot"}],
    [{"type": "link", "text": "Бот «Миланкор»", "url": "https://max.ru/ССЫЛКА_НА_БОТА"}],
    [{"type": "link", "text": "Бот «Ястребов»", "url": "https://max.ru/ССЫЛКА_НА_БОТА"}],
    [{"type": "callback", "text": "⬅️ Назад", "payload": "institutions"}],
    [{"type": "callback", "text": "🏠 На главную", "payload": "back_to_menu"}],
]

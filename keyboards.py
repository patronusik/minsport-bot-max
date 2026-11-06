# Клавиатуры в формате MAX API: [[{"type": "callback", "text": "...", "payload": "..."}, ...], ...]
# Для URL-кнопок: {"type": "link", "text": "...", "url": "..."}

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

# ... остальные клавиатуры (calendar_kb, athletes_kb, gto_kb, tax_kb и т.д.)
# переделай по тому же принципу: [{"type": "callback"|"link", "text": "...", "payload"|"url": "..."}]

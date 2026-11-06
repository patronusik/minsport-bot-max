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
from handlers.start import is_user_subscribed


def register(dp, bot):

    @dp.callback()
    async def on_callback(cb):
        print(f"CALLBACK: payload={cb.payload} user={getattr(cb, 'user', None)}")

        user_id = None
        if hasattr(cb, "user") and cb.user is not None:
            user_id = getattr(cb.user, "id", None) or (
                cb.user.get("user_id") if isinstance(cb.user, dict) else None
            )
        if user_id is None:
            user_id = getattr(cb, "user_id", None)

        print(f"CALLBACK: resolved user_id={user_id}")

        payload = cb.payload

        # --- ПОДПИСКА ---
        if payload == "check_sub":
            subscribed = await is_user_subscribed(user_id)
            if subscribed:
                await bot.send_message(
                    user_id=user_id,
                    text=TEXT_WELCOME,
                    reply_markup=main_menu_kb,
                    format="markdown"
                )
            else:
                await bot.send_message(
                    user_id=user_id,
                    text=TEXT_NOT_SUBSCRIBED,
                    reply_markup=subscribe_kb
                )
            return

        # --- НА ГЛАВНУЮ (без проверки подписки, чтобы всегда можно было вернуться) ---
        if payload == "back_to_menu":
            await bot.send_message(user_id=user_id, text=TEXT_WELCOME,
                                   reply_markup=main_menu_kb, format="markdown")
            return

        # --- ДЛЯ ВСЕХ ОСТАЛЬНЫХ ДЕЙСТВИЙ — ПРОВЕРКА ПОДПИСКИ ---
        subscribed = await is_user_subscribed(user_id)
        if not subscribed:
            await bot.send_message(
                user_id=user_id,
                text=TEXT_NOT_SUBSCRIBED,
                reply_markup=subscribe_kb
            )
            return

        # --- РАЗДЕЛ 1: УЧРЕЖДЕНИЯ ---
        if payload == "institutions":
            await bot.send_message(user_id=user_id, text=TEXT_INSTITUTIONS,
                                   reply_markup=institutions_kb, format="markdown")

        elif payload == "inst_kaspiy":
            await bot.send_message(user_id=user_id,
                                   text="🏛 ГАУ АО РЦСА «Каспий»\n\nВыберите подраздел:",
                                   reply_markup=inst_kaspiy_kb, format="markdown")

        elif payload == "inst_volgar":
            await bot.send_message(user_id=user_id,
                                   text="🏛 ГАУ АО РЦСП «Волгарь»\n\nВыберите подраздел:",
                                   reply_markup=inst_volgar_kb, format="markdown")

        elif payload == "inst_zarya":
            await bot.send_message(user_id=user_id,
                                   text="🏛 ГАУ АО РЦСП «Заря Каспия»\n\nВыберите подраздел:",
                                   reply_markup=inst_zarya_kb, format="markdown")

        elif payload == "inst_zvezdny":
            await bot.send_message(user_id=user_id,
                                   text="🏛 ГАУ АО РЦСП «Звёздный»\n\nВыберите подраздел:",
                                   reply_markup=inst_zvezdny_kb, format="markdown")

        elif payload == "inst_winter":
            await bot.send_message(user_id=user_id,
                                   text="🏛 ГАУ АО «Центр зимних видов спорта»\n\nВыберите подраздел:",
                                   reply_markup=inst_winter_kb, format="markdown")

        # --- РАЗДЕЛ 2: КАЛЕНДАРЬ ---
        elif payload == "calendar":
            await bot.send_message(user_id=user_id, text=TEXT_CALENDAR,
                                   reply_markup=calendar_kb, format="markdown")

        elif payload == "cal_astrakhanochka":
            await bot.send_message(user_id=user_id, text=TEXT_CAL_ASTRAKHANOCHKA,
                                   reply_markup=back_to_calendar_kb, format="markdown")

        elif payload == "cal_volgar":
            await bot.send_message(user_id=user_id, text=TEXT_CAL_VOLGAR,
                                   reply_markup=back_to_calendar_kb, format="markdown")

        elif payload == "cal_dinamo":
            await bot.send_message(user_id=user_id, text=TEXT_CAL_DINAMO,
                                   reply_markup=back_to_calendar_kb, format="markdown")

        elif payload == "cal_dinamo_vk":
            await bot.send_message(user_id=user_id, text=TEXT_CAL_DINAMO_VK,
                                   reply_markup=back_to_calendar_kb, format="markdown")

        elif payload == "cal_astrakhan":
            await bot.send_message(user_id=user_id, text=TEXT_CAL_ASTRAKHAN,
                                   reply_markup=back_to_calendar_kb, format="markdown")

        # --- РАЗДЕЛ 3: СПОРТСМЕНАМ ---
        elif payload == "athletes":
            await bot.send_message(user_id=user_id, text=TEXT_ATHLETES,
                                   reply_markup=athletes_kb, format="markdown")

        elif payload == "ranks":
            await bot.send_message(user_id=user_id,
                                   text="🏅 **Присвоение спортивных разрядов и званий**\n\nВыберите подраздел:",
                                   reply_markup=ranks_kb, format="markdown")

        elif payload == "ranks_who":
            await bot.send_message(user_id=user_id, text=TEXT_RANKS_WHO,
                                   reply_markup=back_to_ranks_kb, format="markdown")

        # --- РАЗДЕЛ 4: ГТО ---
        elif payload == "gto_menu":
            await bot.send_message(user_id=user_id, text=TEXT_GTO_MENU,
                                   reply_markup=gto_kb, format="markdown")

        elif payload == "gto_how":
            await bot.send_message(user_id=user_id, text=TEXT_GTO_HOW,
                                   reply_markup=back_to_gto_kb, format="markdown")

        elif payload == "gto_centers":
            await bot.send_message(user_id=user_id, text=TEXT_GTO_CENTERS,
                                   reply_markup=back_to_gto_kb, format="markdown")

        # --- РАЗДЕЛ 5: НАЛОГОВЫЙ ВЫЧЕТ ---
        elif payload == "tax_menu":
            await bot.send_message(user_id=user_id, text=TEXT_TAX_MENU,
                                   reply_markup=tax_kb, format="markdown")

        elif payload == "tax_sport":
            await bot.send_message(user_id=user_id, text=TEXT_TAX_SPORT,
                                   reply_markup=tax_sport_kb, format="markdown")

        # --- РАЗДЕЛ 8: ФЕДЕРАЦИЯМ ---
        elif payload == "federations":
            await bot.send_message(user_id=user_id,
                                   text="🤝 **Федерациям, НКО и частным клубам**\n\nВыберите раздел:",
                                   reply_markup=federations_kb, format="markdown")

        # --- РАЗДЕЛ 9: КОНТАКТЫ ---
        elif payload == "contacts":
            await bot.send_message(user_id=user_id, text=TEXT_CONTACTS,
                                   reply_markup=back_to_menu_kb, format="markdown")

        else:
            print(f"UNHANDLED PAYLOAD: {payload}")

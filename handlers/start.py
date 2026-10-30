import aiohttp
from maxbot.types import Message
from config import TEXT_SUBSCRIBE, TEXT_NOT_SUBSCRIBED, TEXT_WELCOME, CHANNEL_ID, MAX_BOT_TOKEN
from keyboards import subscribe_kb, main_menu_kb


async def is_user_subscribed(user_id: int) -> bool:
    """
    Проверяет, подписан ли пользователь на канал (сообщество).
    Возвращает True, если подписан, и False, если нет.
    """
    url = f"https://platform-api2.max.ru/chats/{CHANNEL_ID}/members"
    headers = {
        "Authorization": MAX_BOT_TOKEN
    }
    params = {
        "user_ids": user_id
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params, ssl=False) as resp:
                if resp.status != 200:
                    print(f"Ошибка API проверки подписки: {resp.status}, {await resp.text()}")
                    return False

                data = await resp.json()
                members = data.get("members", [])

                # Если массив members не пустой — пользователь подписан
                return len(members) > 0
    except Exception as e:
        print(f"Ошибка при проверке подписки: {e}")
        return False


def register(dp, bot):

    @dp.bot_started
    async def on_bot_started(update):
        """Срабатывает при нажатии кнопки 'Начать' в MAX"""
        user_id = update['user']['user_id']
        print(f"BOT_STARTED: user_id={user_id}")
        await bot.send_message(
            user_id=user_id,
            text=TEXT_SUBSCRIBE,
            reply_markup=subscribe_kb,
            format="markdown"
        )

    @dp.message()
    async def on_message(message: Message):
        """Срабатывает на любое текстовое сообщение"""
        print(f"MESSAGE: text={getattr(message, 'text', None)} sender={message.sender.id}")
        await bot.send_message(
            user_id=message.sender.id,
            text=TEXT_SUBSCRIBE,
            reply_markup=subscribe_kb,
            format="markdown"
        )

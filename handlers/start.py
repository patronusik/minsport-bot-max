import os
import asyncio
import aiohttp
import ssl
from config import TEXT_SUBSCRIBE, TEXT_NOT_SUBSCRIBED, TEXT_WELCOME, CHANNEL_ID, MAX_BOT_TOKEN
from keyboards import main_menu_kb, subscribe_kb

API_URL = "https://platform-api2.max.ru"

def get_ssl_context():
    return ssl.create_default_context(cafile="/etc/ssl/certs/ca-certificates.crt")

async def api_request(method, path, params=None, json_data=None):
    url = f"{API_URL}{path}"
    headers = {
        "Authorization": MAX_BOT_TOKEN,
        "Content-Type": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, headers=headers, params=params, json=json_data, ssl=get_ssl_context()) as resp:
            text = await resp.text()
            print(f"API {method} {path} -> {resp.status}: {text[:300]}", flush=True)
            return resp.status, text

async def send_message(user_id, text, keyboard=None, message_id=None):
    """Отправляет новое сообщение или редактирует существующее."""
    if message_id:
        # Редактирование
        body = {"text": text, "format": "markdown"}
        if keyboard:
            body["attachments"] = [{"type": "inline_keyboard", "payload": {"buttons": keyboard}}]
        return await api_request("PUT", f"/messages?message_id={message_id}", json_data=body)
    else:
        # Новое сообщение
        body = {"text": text, "format": "markdown"}
        if keyboard:
            body["attachments"] = [{"type": "inline_keyboard", "payload": {"buttons": keyboard}}]
        return await api_request("POST", f"/messages?user_id={user_id}", json_data=body)

async def answer_callback(callback_id):
    await api_request("POST", "/answers", json_data={"callback_id": callback_id})

async def is_user_subscribed(user_id):
    # Прямой запрос к API проверки подписки (если работает) или заглушка True для теста
    # Временно можно вернуть True, чтобы меню работало
    return True

async def run_bot():
    # Проверяем подключение
    status, _ = await api_request("GET", "/me")
    if status != 200:
        print("❌ Не удалось подключиться к API MAX", flush=True)
        return

    print("✅ Бот запущен, начинаем polling...", flush=True)
    marker = None
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                params = {"timeout": 30, "types": "message_created,message_callback,bot_started"}
                if marker:
                    params["marker"] = marker
                async with session.get(f"{API_URL}/updates", headers={"Authorization": MAX_BOT_TOKEN}, params=params, ssl=get_ssl_context()) as resp:
                    if resp.status != 200:
                        print(f"Polling error: {resp.status}", flush=True)
                        await asyncio.sleep(5)
                        continue
                    data = await resp.json()
                    updates = data.get("updates", [])
                    marker = data.get("marker")
                    for upd in updates:
                        await handle_update(upd)
            except Exception as e:
                print(f"Polling exception: {e}", flush=True)
                await asyncio.sleep(5)

async def handle_update(upd):
    upd_type = upd.get("update_type")
    if upd_type == "message_callback":
        cb = upd.get("callback", {})
        callback_id = cb.get("callback_id")
        payload = cb.get("payload")
        user_id = cb.get("user", {}).get("user_id")
        message = cb.get("message", {})
        message_id = message.get("mid") or message.get("id")
        
        print(f"CALLBACK: payload={payload}, message_id={message_id}", flush=True)
        await answer_callback(callback_id)
        
        # Передаём в menu
        await menu.handle_menu(payload, user_id, message_id)
        
    elif upd_type == "message_created":
        msg = upd.get("message", {})
        user_id = msg.get("sender", {}).get("user_id")
        text = msg.get("text", "")
        print(f"MESSAGE: {text} from {user_id}", flush=True)
        # Отправляем приветствие с подпиской
        await send_message(user_id, TEXT_SUBSCRIBE, keyboard=subscribe_kb)
        
    elif upd_type == "bot_started":
        user_id = upd.get("user", {}).get("user_id")
        print(f"BOT_STARTED: {user_id}", flush=True)
        await send_message(user_id, TEXT_SUBSCRIBE, keyboard=subscribe_kb)

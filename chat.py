import os
import sys
import base64
import config
import asyncio
import aioconsole
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from userbot import Client
from utils import crypto

username = sys.argv[1]
session = PromptSession()

# Закрытый и открытый ключи
global private_key, public_key, symmetric_key
private_key, public_key, symmetric_key = crypto.generate_keys()
public_key2 = None
symmetric_key2 = None

print('Chat with ' + username)
print()

# Удаление файлов сообщений прошлой переписки
if os.path.exists(config.INCOMING_MESSAGE_PATH):
    os.remove(config.INCOMING_MESSAGE_PATH)

if os.path.exists(config.OUTGOING_MESSAGE_PATH):
    os.remove(config.OUTGOING_MESSAGE_PATH)

# Читаем содержимое входящего сообщения из текстового файла
def read_incoming_message():
    with open(config.INCOMING_MESSAGE_PATH, 'r', encoding='utf-8') as file:
        message = file.read()
        return message

# Читаем содержимое исходящего сообщения из текстового файла
def read_outgoing_message():
    with open(config.OUTGOING_MESSAGE_PATH, 'r', encoding='utf-8') as file:
        message = file.read()
        return message

# Сохраняем содержимое входящего сообщения в текстовый файл
def save_incoming_message(message):
    with open(config.INCOMING_MESSAGE_PATH, 'w', encoding='utf-8') as file:
        file.write(message)

# Сохраняем содержимое исходящего сообщения в текстовый файл
def save_outgoing_message(message):
    with open(config.OUTGOING_MESSAGE_PATH, 'w', encoding='utf-8') as file:
        file.write(message)

# Отправляем наш публичный ключ
async def send_public_key():
    # print('The public key has been sent to the interlocutor.')
    pem = crypto.encode_public_key(public_key)
    await telescream.client.send_message(username, 'public_key ' + pem)

# Отправляем наш зашифрованный симметричный ключ
async def send_encrypted_symmetric_key():
    # print('The encrypted symmetric key has been sent to the interlocutor.')
    encrypted_symmetric_key = crypto.encrypt_symmetric_key(public_key2, symmetric_key)
    encrypted_symmetric_key = base64.b64encode(encrypted_symmetric_key).decode('utf-8')
    await telescream.client.send_message(username, 'symmetric_key ' + encrypted_symmetric_key)

# Получаем публичный ключ нашего собеседника
async def receive_public_key(pem2):
    # print('The interlocutor\'s public key has been received.')
    global public_key2
    public_key2 = crypto.decode_public_key(pem2)

    await send_encrypted_symmetric_key()

# Получаем зашифрованный симметричный ключ нашего собеседника
async def receive_encrypted_symmetric_key(encrypted_symmetric_key):
    # print('The interlocutor\'s public key has been received.')
    global symmetric_key2
    symmetric_key2 = base64.b64decode(encrypted_symmetric_key.encode('utf-8'))
    symmetric_key2 = crypto.decrypt_symmetric_key(private_key, symmetric_key2)

# Запуск Telescream
async def start_telescream():
    global telescream
    telescream = Client(
        config.SESSION_NAME,
        config.API_ID,
        config.API_HASH,
        system_version=config.SYSTEM_VERSION,
        device_model=config.DEVICE_MODEL,
        app_version=config.APP_VERSION
    )

    @telescream.client.on(telescream.events.NewMessage(from_users=username))
    async def handler(event):
        if hasattr(event, 'raw_text'):
            content = event.raw_text
            if content.startswith('public_key'):
                pem2 = content.split(' ', maxsplit=1)[1]
                await receive_public_key(pem2)
            elif content.startswith('symmetric_key'):
                encrypted_symmetric_key = content.split(' ', maxsplit=1)[1]
                await receive_encrypted_symmetric_key(encrypted_symmetric_key)
            else:
                save_incoming_message(content)

    await telescream.client.connect()
    me = await telescream.client.get_me()
    async for message in telescream.client.iter_messages(username, limit=1):
        content = message.text
        if me.id != message.sender_id:
            if content.startswith('public_key'):
                pem2 = content.split(' ', maxsplit=1)[1]
                await receive_public_key(pem2)
            elif content.startswith('symmetric_key'):
                encrypted_symmetric_key = content.split(' ', maxsplit=1)[1]
                await receive_encrypted_symmetric_key(encrypted_symmetric_key)

        await send_public_key()
    await telescream.client.disconnect()
    await telescream.start_client()

# Консольный чат
async def console_chat():
    while True:
        if symmetric_key2 is not None:
            with patch_stdout():
                message = await session.prompt_async('>> ')
                save_outgoing_message(message)
        else:
            await asyncio.sleep(1)

# Читаем исходящие сообщения и отправляем собеседнику
async def watch_incoming():
    while True:
        if os.path.exists(config.INCOMING_MESSAGE_PATH):
            message = read_incoming_message()
            message = base64.b64decode(message.encode('utf-8'))
            message = crypto.decrypt_message(symmetric_key, message)
            print(message)
            os.remove(config.INCOMING_MESSAGE_PATH)

        if os.path.exists(config.OUTGOING_MESSAGE_PATH):
            message = read_outgoing_message()
            message = crypto.encrypt_message(symmetric_key2, message)
            message = base64.b64encode(message).decode('utf-8')
            await telescream.client.send_message(username, message)
            os.remove(config.OUTGOING_MESSAGE_PATH)

        await asyncio.sleep(1)

async def main():
    await asyncio.gather(
        start_telescream(),
        console_chat(),
        watch_incoming()
    )

try:
    asyncio.run(main())
except Exception as e:
    print(e)
    input()
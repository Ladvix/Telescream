import config
import asyncio
from telethon import TelegramClient, events, errors

class Client:
    def __init__(self, session_name: str, api_id: str, api_hash: str, system_version: str, device_model: str, app_version: str):
        self.client = TelegramClient(
            session_name,
            api_id,
            api_hash,
            system_version=system_version,
            device_model=device_model,
            app_version=app_version
        )
        self.events = events
        self.errors = errors

    # Отправка кода подтверждения
    async def send_code(self, phone_number: str):
        try:
            await self.client.connect()
            sent = await self.client.send_code_request(phone_number)

            return sent.phone_code_hash
        except errors.rpcerrorlist.ApiIdInvalidError:
            return 'the api_id/api_hash combination is invalid'

    # Проверка кода подтверждения
    async def verify_code(self, code: str, phone_code_hash: str, password_2fa: str):
        try:
            if password_2fa is not None:
                await self.client.sign_in(password=password_2fa)
                await self.client.disconnect()
            else:
                await self.client.sign_in(code=code, phone_code_hash=phone_code_hash)
            return True
        except errors.rpcerrorlist.FloodWaitError as error:
            return f'floodwait error {error.seconds}'
        except errors.PhoneCodeInvalidError:
            return 'invalid phone code'
        except errors.PhoneCodeExpiredError:
            return 'the phone code has expired'
        except errors.PasswordHashInvalidError:
            return 'invalid 2fa'
        except errors.SessionPasswordNeededError:
            return '2fa'

    # Запуск клиента
    async def start_client(self):
        await self.client.start()
        await self.client.run_until_disconnected()
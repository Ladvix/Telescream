import time
import config
from userbot import Client
from utils import credentials, console_helper, credentials

async def do():
    # Получение необходимых данных от пользователя
    api_id = console_helper.color_input('Enter the API ID >> ')
    api_hash = console_helper.color_input('Enter the API HASH >> ')
    phone_number = console_helper.color_input('Enter the phone number >> ')

    # Проверка валидности данных
    is_credentials_valid = await credentials.validate(api_id, api_hash, phone_number)
    if not is_credentials_valid:
        print()
        console_helper.warning('Check the validity of your credentials.')
        return

    # Инициализация клиента
    telescream = Client(
        config.SESSION_NAME,
        api_id,
        api_hash,
        system_version=config.SYSTEM_VERSION,
        device_model=config.DEVICE_MODEL,
        app_version=config.APP_VERSION
    )

    # Отправляем код подтверждения
    phone_code_hash = await telescream.send_code(phone_number)
    if phone_code_hash != 'the api_id/api_hash combination is invalid':
        global password_2fa
        password_2fa = None
        code = console_helper.color_input('Enter the confirmation code >> ')
        
        # Проверяем правильность введенного кода подтверждения
        while True:
            response = await telescream.verify_code(code, phone_code_hash, password_2fa)

            if response is True:
                # Успешный вход
                await credentials.save(api_id, api_hash, phone_number)
                print()
                console_helper.done('You have successfully logged in.')
                return
            elif response == '2fa':
                # Требуется двухфакторная аутентификация
                password_2fa = console_helper.color_input('Enter the password 2fa >> ')
            elif response == 'invalid 2fa':
                # Пароль неверный
                console_helper.error('The 2fa password was entered incorrectly.')
            elif response == 'invalid phone code' or response == 'the phone code has expired':
                # Код неверный, либо истёкший
                print()
                console_helper.error('The code was entered incorrectly, or the code expired.')
                return
            elif response.startswith('floodwait error'):
                # Слишком много попыток входа
                seconds = response.split(' ')[2]
                print()
                console_helper.error(f'Floodwait error. Wait {seconds} seconds')
                return
    else:
        # Комбинация API ID/API HASH неверна
        print()
        console_helper.error('The api_id/api_hash combination is invalid.')
        return
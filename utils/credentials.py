import re
import time
import config
from utils import json_helper

# Проверка валидности API ID, API HASH и номера телефона
async def validate(api_id: str, api_hash: str, phone_number: str) -> bool:
    valid = True
    validated_data = {}

    # Проверка API ID
    try:
        api_id = int(api_id)
        if api_id <= 0:
            raise ValueError
        validated_data['api_id'] = api_id
    except (TypeError, ValueError):
        valid = False

    # Проверка API HASH
    if not isinstance(api_hash, str):
        valid = False
    elif not re.fullmatch(r'[0-9a-fA-F]{32}', api_hash):
        valid = False
    else:
        validated_data['api_hash'] = api_hash

    # Проверка номера телефона
    if not isinstance(phone_number, str):
        valid = False
    else:
        cleaned_phone = re.sub(r'[\s\-\(\)\+]', '', phone_number)
        if not cleaned_phone.isdigit():
            valid = False
        else:
            if not phone_number.strip().startswith('+'):
                valid = False
            else:
                if not re.fullmatch(r'\+\d{8,15}', phone_number.strip()):
                    valid = False
                else:
                    validated_data['phone'] = phone_number.strip()

    return valid

# Запись учетных данных в json файл
async def save(api_id: str, api_hash: str, phone_number: str):
    credentials = {
        'api_id': api_id,
        'api_hash': api_hash,
        'phone_number': phone_number,
        'time': int(time.time())
    }
    json_helper.write(config.CREDENTIALS_PATH, credentials)
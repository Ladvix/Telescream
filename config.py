import os
from utils import json_helper

ABS_PATH = os.path.dirname(__file__)
TEMPLATES_PATH = os.path.join(ABS_PATH, 'templates')
INCOMING_MESSAGE_PATH = os.path.join(ABS_PATH, 'incoming_message.txt')
OUTGOING_MESSAGE_PATH = os.path.join(ABS_PATH, 'outgoing_message.txt')
CREDENTIALS_PATH = os.path.join(ABS_PATH, 'credentials.json')

if os.path.exists(CREDENTIALS_PATH):
    credentials = json_helper.read(CREDENTIALS_PATH)
    API_ID = credentials['api_id']
    API_HASH = credentials['api_hash']
    PHONE_NUMBER = credentials['phone_number']

SESSION_NAME = 'telescream'

DEVICE_MODEL = 'Telescream'
SYSTEM_VERSION = 'Telescream 1.0.0'
APP_VERSION = '11.14.1'
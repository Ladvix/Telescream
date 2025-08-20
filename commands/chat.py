import os
import config
import subprocess
from utils import console_helper

async def do(command):
    args = command.split(' ', maxsplit=1)
    if len(args) > 1:
        username = args[1]
        if not username.startswith('@'): username = '@' + username
        # Открываем отдельное консольное окно для чата
        process = subprocess.Popen(
            ['python', os.path.join(config.ABS_PATH, 'chat.py'), username],
            creationflags=0x00000010
        )
        console_helper.done('The chat has been opened successfully.')
    else:
        console_helper.warning('Enter an username: ' + console_helper.primary('/chat') + ' @username')
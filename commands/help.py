from utils import console_helper

async def do():
    console_helper.message(
    console_helper.primary('/start') + '          -> Launch a userbot' + '\n' + 
    console_helper.primary('/chat @username') + ' -> Open the last created chat' + '\n' + 
    console_helper.primary('/help') + '           -> Display the documentation on the commands in the console'
    )
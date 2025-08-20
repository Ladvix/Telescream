import asyncio
import threading
import aioconsole
from commands import start, help, chat
from utils import credentials, json_helper, console_helper

# Запуск консоли
async def start_console():
    while True:
        command = await aioconsole.ainput('>> ')
        print()
        if command == '/start':
            await start.do()
        elif command.startswith('/chat'):
            await chat.do(command)
        elif command == '/help':
            await help.do()
        print()

async def main():
    console_helper.clear_console()
    console_helper.print_banner()

    threading.Thread(target=asyncio.run_coroutine_threadsafe, args=(start_console(), loop)).start()

if __name__ == '__main__':
    try:
        global loop
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        loop.run_until_complete(main())
        loop.run_forever()
    except Exception as e:
        print(e)
import os
import config

valid_hex = '0123456789ABCDEF'.__contains__

colors = {
    'primary': "#EB373A",
    'error': '#FF1E00',
    'warning': "#FF7B00",
    'done': "#00E404",
    'message': "#EFEFEFFF"
}

def cleanhex(data):
    return ''.join(filter(valid_hex, data.upper()))

def fore_fromhex(text: str, hex_color: str) -> str:
    hex_int = int(cleanhex(hex_color), 16)
    return '\x1B[38;2;{};{};{}m{}\x1B[0m'.format(hex_int>>16, hex_int>>8&0xFF, hex_int&0xFF, text)

def back_fromhex(text: str, hex_color: str) -> str:
    hex_int = int(cleanhex(hex_color), 16)
    return '\033[48;2;{};{};{}m{}\033[0m'.format(hex_int>>16, hex_int>>8&0xFF, hex_int&0xFF, text)

def color_input(text: str):
    return input(fore_fromhex('\033[1m' + str(text), colors['primary']))

def error(message: str):
    print(fore_fromhex('[-] ' + message, colors['error']))

def warning(message: str):
    print(fore_fromhex('[!] ' + message, colors['warning']))

def done(message: str):
    print(fore_fromhex('[+] ' + message, colors['done']))

def message(message: str):
    print(fore_fromhex(message, colors['message']))

def primary(message: str):
    return fore_fromhex('\033[1m' + message, colors['primary'])

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    with open(os.path.join(config.TEMPLATES_PATH, 'banner.txt'), 'r') as file:
        banner = file.read()
        print(fore_fromhex('\033[1m' + banner, colors['primary']))
        print()
        print(primary('Welcome to the Telescream Telegram client. Start your secret messaging right now!'))
        print(fore_fromhex('Join to our community - ' + '\033[4m' + 'https://t.me/telescream.', colors['message']))
        print(fore_fromhex('Send ' + primary('/help') + ' to find out the details.', colors['message']))
        print()
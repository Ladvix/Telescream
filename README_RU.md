<div align="center">

  # Telescream

  <p>
    <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
    <img src="https://img.shields.io/badge/Telegram-Userbot-blue.svg" alt="Telegram Userbot">
  </p>

  [English](README.md) | **Русский**

  <img style="width:100%; height:auto;" alt="image" src="https://github.com/user-attachments/assets/057895c1-2833-4451-a2db-9f8ededad8aa" />

</div>

Telescream - это защищенный пользовательский юзербот Telegram, который позволяет вести сквозные зашифрованные приватные чаты между двумя пользователями. Он использует гибридную схему шифрования, сочетающую RSA (асимметричное шифрование) для обмена ключами и AES (симметричное шифрование) для быстрого и безопасного шифрования сообщений, что гарантирует конфиденциальность ваших разговоров и защиту от прослушивания.

## Особенности:
- Сквозное шифрование (E2EE) для чатов один на один
- Обмен ключами RSA-2048 и шифрование сообщений AES-256-CBC
- Автоматический обмен открытым ключом и согласование сеансового ключа.
- Обмен зашифрованными сообщениями в режиме реального времени с помощью файловой связи
- Создан на основе Telethon
- Консольный интерфейс чата

## Как это работает:

Пользователи автоматически обмениваются открытыми ключами.
Общий симметричный ключ шифруется с помощью открытого ключа получателя и безопасно отправляется.
Все сообщения перед отправкой шифруются локально.
Расшифровать и прочитать сообщения может только тот, кому они предназначены.

## Конфиденциальность превыше всего
Сообщения отправляются в уже зашифрованном виде. Даже Telegram не сможет прочитать ваши чаты.

## Настройка и использование
Предназначен для технических пользователей, которые ценят конфиденциальность. Требуется Python, криптографические библиотеки RSA/AES и учетная запись в Telegram.

## Установка

```bash
# Clone the repository
git clone https://github.com/Ladvix/Telescream.git
cd Telescream

# Install dependencies
pip install -r requirements.txt

# Run the userbot
python main.py
```

## Лицензия

Распространяется [под лицензией MIT](https://github.com/Ladvix/Telescream/blob/main/LICENSE).

## Ссылки

- <a href="https://t.me/telescream"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white" alt="Telegram Channel"></a>

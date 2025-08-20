# Telescream

<p align="center">
  <img style="width:100%; height:auto;" alt="image" src="https://github.com/user-attachments/assets/057895c1-2833-4451-a2db-9f8ededad8aa" />
</p>

Telescream is a secure Telegram userbot that enables end-to-end encrypted private chats between two users. Built with cryptography in mind, it uses a hybrid encryption scheme combining RSA (asymmetric) for key exchange and AES (symmetric) for fast, secure message encryption — ensuring your conversations stay private and safe from eavesdropping.

##@ 🚀 Features:
✅ End-to-end encryption (E2EE) for one-on-one chats
🔐 RSA-2048 key exchange and AES-256-CBC message encryption
🤝 Automatic public key sharing and session key negotiation
💬 Real-time encrypted messaging via file-based communication
🧩 Built on Telethon for seamless Telegram integration
🖥️ Console-based chat interface for simplicity and privacy

### 🔧 How It Works:

Users exchange public keys automatically.
A shared symmetric key is encrypted with the recipient’s public key and sent securely.
All messages are encrypted locally before being sent.
Only the intended recipient can decrypt and read the messages.

### 🛡️ Privacy First
No messages are stored on servers. Everything is encrypted client-side — not even Telegram can read your chats.

### 📦 Setup & Usage
Designed for technical users who value privacy. Requires Python, RSA/AES crypto libraries, and a Telegram account.

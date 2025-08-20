from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

# Генерация пары ключей (закрытый и открытый)
def generate_keys():
    # Приватный и публичный ключ
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    # Генерация ключа симметричного шифрования
    symmetric_key = Fernet.generate_key()

    return private_key, public_key, symmetric_key

# Преобразование bytes публичного ключа в str
def encode_public_key(public_key: bytes) -> str:
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return pem.decode('utf-8')

# Преобразование str публичного ключа в bytes
def decode_public_key(pem: str) -> bytes:
    pem_bytes = pem.encode('utf-8')
    public_key = serialization.load_pem_public_key(pem_bytes)

    return public_key

# Шифрование симметричного ключа открытым ключом
def encrypt_symmetric_key(public_key: bytes, symmetric_key: bytes) -> bytes:
    encrypted_symmetric_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_symmetric_key

# Расшифровка симметричного ключа закрытым ключом
def decrypt_symmetric_key(private_key: bytes, symmetric_key: bytes) -> bytes:
    decrypted_symmetric_key = private_key.decrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return decrypted_symmetric_key

# Шифрование сообщения симметричным ключом
def encrypt_message(symmetric_key: bytes, message: str) -> bytes:
    cipher = Fernet(symmetric_key)
    encrypted_message = cipher.encrypt(message.encode())

    return encrypted_message

# Расшифровка сообщения симметричным ключом
def decrypt_message(symmetric_key: bytes, message: bytes) -> str:
    cipher = Fernet(symmetric_key)
    decrypted_message = cipher.decrypt(message)

    return decrypted_message.decode()
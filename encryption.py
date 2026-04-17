from cryptography.fernet import Fernet

KEY = b'Rk9kS3l2dE9nT0p2RkV2eXh5cFZtQkR3eWd4Z2xqM3A='

cipher = Fernet(KEY)

def encrypt_message(message: bytes) -> bytes:
    return cipher.encrypt(message)

def decrypt_message(token: bytes) -> bytes:
    return cipher.decrypt(token)
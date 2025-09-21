import base64
import hashlib
import secrets
import datetime

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def generate_nonce(length=16):
    return secrets.token_hex(length)


def get_timestamp():
    return datetime.datetime.now(datetime.datetime.utc).strftime("%Y%m%d%H%M%S")


def build_sign_string(fields: list, data: dict) -> str:
    """
    Azericard qaydasına görə: len(value) + value ardıcıllığı ilə string qurulur
    """
    sign_parts = []
    for field in fields:
        value = str(data.get(field, ""))
        sign_parts.append(f"{len(value)}{value}")
    return "".join(sign_parts)


def generate_psign(private_key_path: str, fields: list, data: dict) -> str:
    """
    P_SIGN yaratmaq (private key ilə imzalanır)
    """
    sign_string = build_sign_string(fields, data)

    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    signature = private_key.sign(
        sign_string.encode("utf-8"),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    return base64.b64encode(signature).decode("utf-8")


def verify_psign(public_key_path: str, fields: list, data: dict) -> bool:
    """
    P_SIGN yoxlamaq (bankın public key ilə)
    """
    try:
        p_sign = data.pop("P_SIGN")
    except KeyError:
        return False

    sign_string = build_sign_string(fields, data)
    signature = base64.b64decode(p_sign)

    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    try:
        public_key.verify(
            signature,
            sign_string.encode("utf-8"),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

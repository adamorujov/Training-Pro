import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def md5_sign(data: str, secret: str) -> str:
    """
    Returns MD5 signature of data + secret
    """
    raw = f"{data}{secret}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest().upper()

def load_public_key(path: str):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())

def load_private_key(path: str):
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

def rsa_sign(private_key, data: str) -> str:
    signature = private_key.sign(
        data.encode("utf-8"),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return signature.hex()

def rsa_verify(public_key, data: str, signature: str) -> bool:
    try:
        public_key.verify(
            bytes.fromhex(signature),
            data.encode("utf-8"),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False


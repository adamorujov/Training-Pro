# payments/utils/azeri_crypto.py
import os
import binascii
import base64
from typing import Optional
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from pathlib import Path
import secrets


def fix_pem_newlines(path: str):
    """
    Read the PEM and normalize newlines to '\n' (like Java's fixPublicKeyFile).
    Overwrites the file in-place.
    """
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    text = text.replace("\r\n", "\n")
    p.write_text(text, encoding="utf-8")


def load_private_key(path: str):
    """
    Loads PKCS8 private key from PEM (no password).
    """
    fix_pem_newlines(path)
    with open(path, "rb") as f:
        data = f.read()
    return serialization.load_pem_private_key(data, password=None, backend=default_backend())


def load_public_key(path: str):
    """
    Load X509 public key from PEM.
    """
    fix_pem_newlines(path)
    with open(path, "rb") as f:
        data = f.read()
    return serialization.load_pem_public_key(data, backend=default_backend())


def hex_to_bytes(hexstr: str) -> bytes:
    return binascii.unhexlify(hexstr)


def bytes_to_hex(b: bytes) -> str:
    return binascii.hexlify(b).decode("ascii")  # lowercase hex — matches Java


def generate_nonce(length: int = 16) -> str:
    # Java produced hex chars via SecureRandom.nextInt(16) -> one hex nibble per char
    # Equivalent: generate length nibbles -> length hex characters
    return secrets.token_hex((length + 1) // 2)[:length]


# ---------- MAC / P_SIGN builders (match Java order) ----------

def build_request_sign_body(amount: str,
                            currency: str,
                            terminal: str,
                            trtype: str,
                            timestamp: str,
                            nonce: str,
                            merch_url: str) -> str:
    """
    Build signBody (length + value) for fields:
    AMOUNT, CURRENCY, TERMINAL, TRTYPE, TIMESTAMP, NONCE, MERCH_URL
    """
    parts = []
    for v in (amount, currency, terminal, trtype, timestamp, nonce, merch_url):
        s = "" if v is None else str(v)
        parts.append(str(len(s)) + s)
    return "".join(parts)


def build_callback_sign_body(amount: Optional[str],
                             terminal: Optional[str],
                             approval: Optional[str],
                             rrn: Optional[str],
                             int_ref: Optional[str]) -> str:
    """
    Java verify used:
      (amount == null ? "-" : length+amount) +
      (terminal == null ? "-" : length+terminal) +
      (approval == null ? "-" : length+approval) +
      (rrn == null ? "-" : length+rrn) +
      (intRef == null ? "-" : length+intRef)
    So if a field is missing -> "-" literal; otherwise length+value.
    """
    out = []
    fields = (amount, terminal, approval, rrn, int_ref)
    for v in fields:
        if v is None or v == "":
            out.append("-")
        else:
            s = str(v)
            out.append(str(len(s)) + s)
    return "".join(out)


def sign_with_private_key_hex(sign_body: str, private_key_path: str) -> str:
    """
    Sign sign_body using SHA256withRSA (PKCS#1 v1.5). Return lowercase hex string.
    Mirrors Java's generatePSign -> hex lowercase.
    """
    priv = load_private_key(private_key_path)
    signature = priv.sign(
        sign_body.encode("utf-8"),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return bytes_to_hex(signature)


def verify_with_public_key_hex(sign_body: str, signature_hex: str, public_key_path: str) -> bool:
    """
    Verify signature_hex (hex string) over sign_body using SHA256withRSA and public key PEM.
    Mirrors Java's verify and verifyPSign methods.
    """
    pub = load_public_key(public_key_path)
    sig = hex_to_bytes(signature_hex)
    try:
        pub.verify(sig, sign_body.encode("utf-8"), padding.PKCS1v15(), hashes.SHA256())
        return True
    except Exception:
        return False



# generate_key.py
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_keys(private_path="private_key.pem", public_path="public_key.pem", bits=3072):
    key = rsa.generate_private_key(public_exponent=65537, key_size=bits)
    priv_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    pub_pem = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(private_path, "wb") as f:
        f.write(priv_pem)
    with open(public_path, "wb") as f:
        f.write(pub_pem)
    print(f"✅ Generated keys: {private_path}, {public_path}")

if __name__ == "__main__":
    generate_keys()

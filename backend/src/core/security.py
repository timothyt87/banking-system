from passlib.hash import bcrypt


# Hash Password
def hash_password(password_text: str) -> str:
    hashed_password = bcrypt.hash(password_text)
    return hashed_password


# Verify Password
def verify_password(password_text: str, hashed_password: str) -> bool:
    if bcrypt.verify(password_text, hashed_password):
        return True
    return False

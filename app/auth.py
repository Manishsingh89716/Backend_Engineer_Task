'''import all libraries'''

from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30   #time for which the token is valid
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")    #it reads the hash passwords

'''define function for storing the string password in hashing form'''
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

'''define function that compares text password with hash password'''
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

'''define function for creation of token using user id and password and also ensures the validity of token'''
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

'''define function that verify user cetails for token acess'''
def decode_access_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
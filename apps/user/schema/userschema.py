from pydantic import BaseModel, EmailStr, validator


class UserIN(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password1: str
    password2: str
    national_id: str

    @validator('password1')
    def password_length(cls, v, values, **kwargs):
        if len(v) < 8:
            raise ValueError('password must be at least 8 characters!')
        else:
            return v

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator('national_id')
    def national_id_length(cls, nid, values, **kwargs):
        if len(nid) != 10:
            raise ValueError('national ID must be exactly 10 characters!')
        else:
            return nid


class UserOut(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    national_id: str


class UserInDB(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    hashed_password: str
    national_id: str


class UserLogIn(BaseModel):
    username: str
    password: str

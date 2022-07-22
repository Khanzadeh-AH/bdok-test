from ..schema.userschema import UserIN, UserOut, UserInDB
from db.mongodb import db
from fastapi import APIRouter, Depends
from bson import ObjectId
from passlib.hash import pbkdf2_sha256
from apps.user.views.userauth import get_current_user

router = APIRouter()


@router.post('/user', tags=["User CRUD"])
async def create_user(user: UserIN):
    hashed_password = pbkdf2_sha256.hash(user.password1)
    user_in_db = UserInDB(**user.dict(), hashed_password=hashed_password)
    res = await db.client['bdokdb']['test_user'].insert_one(user_in_db.dict())
    return {'id': str(res.inserted_id), 'username': user.username}


@router.put('/user', tags=["User CRUD"])
async def update_one(user: UserIN, current_user=Depends(get_current_user)):
    c_user = UserOut(**current_user)
    hashed_password = pbkdf2_sha256.hash(user.password1)
    user_in_db = UserInDB(**user.dict(), hashed_password=hashed_password)
    res = await db.client['bdokdb']['test_user'].replace_one({"username": c_user.username}, user_in_db.dict())
    return res.raw_result


@router.delete('/user', tags=["User CRUD"])
async def delete_one(current_user=Depends(get_current_user)):
    user = UserOut(**current_user)
    res = await db.client['bdokdb']['test_user'].delete_one({"username": user.username})
    return res.raw_result

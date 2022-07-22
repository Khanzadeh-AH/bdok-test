from ..schema.userschema import UserIN, UserOut, UserInDB
from db.mongodb import db
from fastapi import APIRouter
from bson import ObjectId
from passlib.hash import pbkdf2_sha256

router = APIRouter()


@router.get('/user/{uid}', tags=["User CRUD"])
async def retrieve_one(uid: str):
    res = await db.client['bdokdb']['test_user'].find_one({"_id": ObjectId(uid)})
    return UserOut(**res).dict()


@router.post('/user', tags=["User CRUD"])
async def create_user(user: UserIN):
    hashed_password = pbkdf2_sha256.hash(user.password1)
    user_in_db = UserInDB(**user.dict(), hashed_password=hashed_password)
    res = await db.client['bdokdb']['test_user'].insert_one(user_in_db.dict())
    return {'id': str(res.inserted_id), 'username': user.username}


@router.put('/user/{uid}', tags=["User CRUD"])
async def update_one(uid: str, user: UserIN):
    res = await db.client['bdokdb']['test_user'].replace_one({"_id": ObjectId(uid)}, user.dict())
    return res.raw_result


@router.delete('/user/{uid}', tags=["User CRUD"])
async def delete_one(uid: str):
    res = await db.client['bdokdb']['test_user'].delete_one({"_id": ObjectId(uid)})
    return res.raw_result

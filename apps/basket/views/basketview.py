from ..schemas.basketschema import Basket, BasketInDB
from db.mongodb import db
from fastapi import APIRouter, Depends
from bson import ObjectId
from apps.user.views.userauth import get_current_user
from apps.user.schema.userschema import UserOut

router = APIRouter()


@router.get('/basket', tags=['Basket'], status_code=200)
async def retrieve_all(user=Depends(get_current_user)):
    user = UserOut(**user)
    user_basket = []
    res = db.client['bdokdb']['test_basket'].find({"user": user.dict()})

    async for r in res:
        r['_id'] = str(r['_id'])
        user_basket.append(
            r
        )
    return user_basket


@router.post('/basket', tags=['Basket'], status_code=201)
async def create_basket(basket: Basket, user: UserOut = Depends(get_current_user)):
    b = {**basket.dict(), 'user': user}
    basketindb = BasketInDB(**b)
    res = await db.client['bdokdb']['test_basket'].insert_one(basketindb.dict())
    return {'id': str(res.inserted_id)}


@router.put('/Basket/{bid}', tags=['Basket'])
async def update_one(bid: str, basket: Basket, user=Depends(get_current_user)):
    user = UserOut(**user)
    res = await db.client['bdokdb']['test_basket'].find_one({"_id": ObjectId(bid)})
    if res:
        if res['user']['username'] == user.username:
            b = {**basket.dict(), 'user': user}
            basketindb = BasketInDB(**b)
            up_res = await db.client['bdokdb']['test_basket'].replace_one({"_id": ObjectId(bid)}, basketindb.dict())
            return up_res.raw_result
        else:
            return 'you are not the owner of the basket!'
    else:
        return 'no basket found!'


@router.delete('/Basket/{bid}', tags=['Basket'])
async def delete_one(bid: str, user=Depends(get_current_user)):
    user = UserOut(**user)
    res = await db.client['bdokdb']['test_basket'].find_one({"_id": ObjectId(bid)})

    if res:
        if res['user']['username'] == user.username:
            del_res = await db.client['bdokdb']['test_basket'].delete_one({"_id": ObjectId(bid)})
            return del_res.raw_result
        else:
            return 'you are not the owner of the basket!'
    else:
        return 'no basket found!'

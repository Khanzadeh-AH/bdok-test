from ..schemas.basketschema import Basket
from db.mongodb import db
from fastapi import APIRouter, Response, status
from bson import ObjectId

router = APIRouter()


@router.get('/basket/{bid}', tags=['Basket'], status_code=200)
async def retrieve_one(bid: str):
    res = await db.client['bdokdb']['test_collection'].find_one({"_id": ObjectId(bid)})
    res['_id'] = str(res['_id'])
    return res


@router.post('/basket', tags=['Basket'], status_code=201)
async def create_basket(basket: Basket):
    res = await db.client['bdokdb']['test_collection'].insert_one(basket.dict())
    return {'id': str(res.inserted_id)}


@router.put('/Basket/{bid}', tags=['Basket'])
async def update_one(bid: str, basket: Basket):
    res = await db.client['bdokdb']['test_collection'].replace_one({"_id": ObjectId(bid)}, basket.dict())
    return res.raw_result


@router.delete('/Basket/{bid}', tags=['Basket'])
async def delete_one(bid: str):
    res = await db.client['bdokdb']['test_collection'].delete_one({"_id": ObjectId(bid)})
    return res.raw_result

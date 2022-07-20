from ..schemas.productschema import Product
from db.mongodb import db
from fastapi import APIRouter, Response, status
from bson import ObjectId

router = APIRouter()


@router.get('/product', tags=['Product'], description='retrieve all products.')
async def retrieve_all():
    products = []
    res = db.client['bdokdb']['test_collection'].find()
    async for r in res:
        r['_id'] = str(r['_id'])
        products.append(
            r
        )

    return products


@router.get('/product/{pid}', tags=['Product'])
async def retrieve_one(pid: str):
    res = await db.client['bdokdb']['test_collection'].find_one({"_id": ObjectId(pid)})
    res['_id'] = str(res['_id'])
    return res


@router.post('/product', tags=['Product'], status_code=201)
async def create_product(product: Product):
    res = await db.client['bdokdb']['test_collection'].insert_one(product.dict())
    return {'id': str(res.inserted_id), 'name': product.name}


@router.put('/product/{pid}', tags=['Product'])
async def update_one(pid: str, product: Product):
    res = await db.client['bdokdb']['test_collection'].replace_one({"_id": ObjectId(pid)}, product.dict())
    return res.raw_result


@router.delete('/product/{pid}', tags=['Product'])
async def delete_one(pid: str):
    res = await db.client['bdokdb']['test_collection'].delete_one({"_id": ObjectId(pid)})
    return res.raw_result

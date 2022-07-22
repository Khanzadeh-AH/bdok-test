from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from apps.product.schemas.productschema import Product
from apps.user.schema.userschema import UserOut


class BasketStatus(str, Enum):
    done = 'done'
    pending = 'pending'
    rollback = 'rollback'


class Basket(BaseModel):
    product: Product
    count: int
    created_at: datetime
    updated_at: datetime
    status: BasketStatus


class BasketInDB(Basket):
    user: UserOut

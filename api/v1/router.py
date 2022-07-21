from fastapi import APIRouter
from apps.product.views.productview import router as productrouter
from apps.basket.views.basketview import router as basketrouter

router = APIRouter()
router.include_router(productrouter)
router.include_router(basketrouter)

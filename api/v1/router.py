from fastapi import APIRouter
from apps.product.views.productview import router as productrouter

router = APIRouter()
router.include_router(productrouter)

from fastapi import APIRouter
from apps.product.views.productview import router as productrouter
from apps.basket.views.basketview import router as basketrouter
from apps.user.views.usercrud import router as usercrudrouter
from apps.user.views.userauth import router as userauthrouter

router = APIRouter()
router.include_router(productrouter)
router.include_router(basketrouter)
router.include_router(usercrudrouter)
router.include_router(userauthrouter)

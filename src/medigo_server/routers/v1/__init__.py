from fastapi import APIRouter
from medigo_server.routers.v1.product_router.product_router import product_router
from medigo_server.routers.v1.category_router.category_router import category_router


# ----------------------------- router combination ---------------------------------
router_v1 = APIRouter(
    prefix="/v1"
)

router_v1.include_router(product_router)
router_v1.include_router(category_router)
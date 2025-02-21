"""Import all routers and add them to routers_list."""
from .admin import router as admin_router
from .echo import router as user_router
from .user import router as echo_router


routers_list = [
    admin_router,
    user_router,
    echo_router,  # echo_router must be last
]

__all__ = [
    'routers_list'
]

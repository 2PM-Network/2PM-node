from fastapi import APIRouter

from . import coord, node, task, model

__all__ = ["router"]

router = APIRouter()
router.include_router(task.router)
router.include_router(coord.router)
router.include_router(node.router)
router.include_router(model.model_router)

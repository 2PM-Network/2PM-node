import logging
import os
from fastapi import APIRouter, Query, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from delta_node import db, entity, pool, coord
import sqlalchemy as sa
from typing import Optional, List
import pickle
from pydantic import BaseModel

_logger = logging.getLogger(__name__)

model_router = APIRouter(prefix="/model")


class Vector(BaseModel):
    data: str  # List[float]


class PredictResp(BaseModel):
    inferenceResult: int


def task_result_file(task_id: str) -> Optional[str]:
    result_filename = coord.loc.task_result_file(task_id)
    if os.path.exists(result_filename):
        return result_filename


@model_router.post("/predict/{task_id}", response_model=PredictResp)
async def predict_model(
    task_id: int, vector: Vector, session: AsyncSession = Depends(db.get_session)
):
    q = sa.select(entity.Task).where(entity.Task.id == task_id)
    task: Optional[entity.Task] = (await session.execute(q)).scalar_one_or_none()
    if task is None:
        raise HTTPException(400, f"task {task_id} does not exist")
    result_filename = await pool.run_in_io(task_result_file, task.task_id)
    if result_filename is None:
        raise HTTPException(400, f"task {task_id} is not finished")

    with open(result_filename, "rb") as file:
        result = pickle.load(file)

    # vector.data format: "[1.0, 2.0, 3.0]"
    vector_data = [float(x) for x in vector.data[1:-1].split(",")]
    if task.type == "hlr":
        if len(vector_data) != len(result[0]):
            raise HTTPException(400, "vector length not match model")
        # predict
        return PredictResp(
            inferenceResult=(
                1
                if sum([a * b for a, b in zip(vector_data, result[0])]) > result[1]
                else 0
            )
        )

    elif task.type == "horizontal":
        raise HTTPException(400, "not implemented")
    else:
        raise HTTPException(400, "unknown task type")

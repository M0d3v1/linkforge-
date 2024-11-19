from fastapi import APIRouter
from app.tasks import example_task

router = APIRouter()

@router.post("/generate-task/")
def generate_task():
    task = example_task.delay()
    return {"message": "Task sent!", "task_id": task.id}

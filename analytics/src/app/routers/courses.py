from fastapi import APIRouter
from app.routers import courses

router = APIRouter()

@router.get("/courses")
async def get_courses():
    return {"courses": [{"name": "Python"}, {"name": "Javascript"}]}

@router.get("/courses/{course_id}")
async def get_course_id(course_id: int):
    return {"course_id": course_id}
 
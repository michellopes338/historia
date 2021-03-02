from fastapi import APIRouter

from . import questions, pontuation


router = APIRouter()

router.include_router(questions.router, prefix='/question', tags=['question'])
router.include_router(pontuation.router, prefix='/pontuation', tags=['pontuation'])
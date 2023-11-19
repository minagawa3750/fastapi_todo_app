import logging

from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/test")
def test_function():
    logger.info("サイコーだぜ たまんないだぜ！")
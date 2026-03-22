from fastapi import APIRouter
from app.schemas.message import EchoRequest, EchoResponse

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Hello World"}


@router.post("/echo", response_model=EchoResponse)
def echo_message(payload: EchoRequest):
    return EchoResponse(
        reply=f"Hello {payload.name}",
        original_message=payload.message
    )
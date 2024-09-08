import grpc
import service_pb2_grpc as pb2_grpc
import service_pb2 as pb2

from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/temp",
)

@router.post("/process")
async def process_message(
    message: str = Body(),
):
    with grpc.insecure_channel('gpt:50052') as channel:
        stub = pb2_grpc.GPTServiceStub(channel)
        grpc_request = pb2.GPTRequest(message=message)
        grpc_response = stub.ProcessData(grpc_request)
    return {"reply": grpc_response.reply}

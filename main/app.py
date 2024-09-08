import grpc
import service_pb2_grpc as pb2_grpc
import service_pb2 as pb2
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GPTRequest(BaseModel):
    message: str

@app.post("/process/")
async def process_message(request: GPTRequest):
    with grpc.insecure_channel('gpt:50052') as channel:
        stub = pb2_grpc.GPTServiceStub(channel)
        grpc_request = pb2.GPTRequest(message=request.message)
        grpc_response = stub.ProcessData(grpc_request)
    return {"reply": grpc_response.reply}

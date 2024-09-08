import grpc
from concurrent import futures
import service_pb2_grpc as pb2_grpc
import service_pb2 as pb2


class GPTService(pb2_grpc.GPTServiceServicer):
    def ProcessData(self, request, context):
        response = pb2.GPTResponse()
        response.reply = f"Processed message: {request.message}"
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GPTServiceServicer_to_server(GPTService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

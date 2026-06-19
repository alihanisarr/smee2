from fastapi import FastAPI, WebSocket, Request
import uvicorn

app = FastAPI()

client: WebSocket = None

@app.post("/webhook")
async def webhook(request: Request):
    global client
    data = await request.json()
    if client is not None:
        await client.send_json(data)    
    return {"message":"hello"}

@app.websocket("/tunnel")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    global client
    client = websocket
    try:
        while True:
            data = await websocket.receive_text()
    except Exception as e:
        client = None

    await websocket.send_text("Message received")


if __name__ == "__main__":
    uvicorn.run("server:app", port=5000) 
    
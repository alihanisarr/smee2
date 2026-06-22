from fastapi import FastAPI, WebSocket, Request
import uvicorn

app = FastAPI()

client: WebSocket = None
subscribers = {}

@app.post("/webhook/{subscription_id}")
async def webhook(subscription_id: str, request: Request):
    if subscription_id is not None:
        global client
        data = await request.json()
        subscribers[subscription_id] = data
        if client is not None:
            await client.send_json(data) 
        return {"message":"hello"}   
    else:   
        print("Invalid endpoint, connection not accepted")
        return
    
@app.websocket("/tunnel/{subscription_id}")
async def websocket_endpoint(subscription_id: str, websocket: WebSocket):
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
    
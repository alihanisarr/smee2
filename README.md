# Smee2
A self-hosted webhook relay (Smee.io alternative) that forwards GitHub webhook payloads to WebSocket clients (SCE CICD server) in real time, replacing reliance on smee.io's public infrastructure.

## Setup instructions:
``` 
python -m venv .venv
source ./.venv/bin/activate
python -m pip install fastapi uvicorn 'uvicorn[standard]'
python -m pip freeze > requirements.txt  
```

## How to test
Testing /webhook to ensure that the POST request is received and sent to server:
``` 
    curl -X POST http://localhost:5000/webhook \
    -H "Content-Type: application/json" \
    -H "X-GitHub-Event: push" \
    -d '{"ref": "refs/heads/main", "repository": {"name": "test-repo"}}'
```



Testing /tunnel to ensure that the websocket connection with the server is established:

`websocat ws://127.0.0.1:5000/tunnel`

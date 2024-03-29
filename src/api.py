import uvicorn
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Replace with your client's origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/quiz")
async def handle_post_request(request_data: dict = Body(...)):
    print(request_data)
    print(request_data['selectedCharacteristics'])
    print(type(request_data['selectedCharacteristics']))
    print(request_data['selectedCharacteristics'][0]['label'])

    return {"message": "POST request received"}


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
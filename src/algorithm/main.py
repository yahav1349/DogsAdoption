from generate_df import FinalModel
import uvicorn
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware


def first_run():
    model = FinalModel(True)
    model.save_model()

def usual_run():
    model = FinalModel()
    return model


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
    model = usual_run()
    model_results = model.get_final_results(request_data)

    return model_results


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI
from controllers.support_controller import support_router

app = FastAPI()


app.include_router(support_router)


@app.get("/")
def index():
    return { "status": "success", "message": "server running" }







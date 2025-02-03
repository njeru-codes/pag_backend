from fastapi import FastAPI
from app.routes import users, notify
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.include_router( users.router)
app.include_router(notify.router)

origins = [
    "*"
]  

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
async def root():
    return {'response': "hello world"}

if __name__=="__main__":
    try:
        uvicorn.run( "app.main:app" , host="0.0.0.0", port=9930)
    except Exception as error:
        print( str(error))
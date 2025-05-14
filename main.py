from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import users, courses, documents, vocabulary, segments, feedback, quiz
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Add your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(users.router)
app.include_router(documents.router)
app.include_router(courses.router)
app.include_router(vocabulary.router)
app.include_router(quiz.router)
app.include_router(feedback.router)

@app.get("/")
async def root():
    return {"message": "Welcome Tameri Study AI"}



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.chat_routes import router

app = FastAPI(title="RAG Document QA System")

# ✅ CORS CONFIG (THIS FIXES YOUR ERROR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow all origins (OK for local dev)
    allow_credentials=True,
    allow_methods=["*"],        # allow OPTIONS, POST, etc.
    allow_headers=["*"],
)

app.include_router(router)

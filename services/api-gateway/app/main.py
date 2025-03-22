from fastapi import FastAPI
from app.routes import authentication, fetch, alerts, notifications
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="API Gateway", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Include Routes
app.include_router(authentication.router, prefix="/auth", tags=["Authentication"])
app.include_router(fetch.router, prefix="/stocks", tags=["Stock Data"])
app.include_router(alerts.router, prefix="/alerts", tags=["Stock Alerts"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])

@app.get("/")
def root():
    return {"message": "API Gateway is running"}
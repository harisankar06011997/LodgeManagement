from fastapi import FastAPI
from app.api.routes import auth, users, rooms, bookings

app = FastAPI(title="Lodge Management API")

# Include API routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(rooms.router, prefix="/rooms", tags=["Rooms"])
app.include_router(bookings.router, prefix="/bookings", tags=["Bookings"])

@app.get("/")
def home():
    return {"message": "Welcome to Lodge Management API"}

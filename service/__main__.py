import uvicorn
from .app import ASGIApplication

if __name__ == "__main__":
    uvicorn.run(ASGIApplication)

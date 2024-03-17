from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from mongo_handler import MongoHandler
from models import ShortenURL
from url_generator import generate_short_url
import time
app = FastAPI()

mongo_handler = MongoHandler()

@app.get("/healthcheck")
async def heathcheck():
    return {"message": "working fine"}


@app.get("/")
async def root():
    return {"message": "working fine"}

@app.get("/{short_url}")
async def fetch_url(short_url: str):

    # get the real url from the database
    real_url = mongo_handler.get_real_url(short_url)
    if real_url:
        return RedirectResponse(url=real_url, status_code=302)
    return {"message": "URL not found"}


@app.post("/shorten")
async def shorten(URL: ShortenURL):
    """
    Shorten the given URL and return the shortened URL.
    """
    # check if the URL is already in the database
    if result := mongo_handler.find({"real_url": str(URL.url)}):
        short_url = result.get("_id")
        short_url = f"http://localhost:8000/{short_url}/"
        return {"short_url": short_url}
    short_url = generate_short_url()
    data = {"real_url": str(URL.url), "short_url": short_url, "created_at": int(time.time()),}
    mongo_handler.insert(data, id=short_url)
    short_url = f"http://localhost:8000/{short_url}/"
    return {"short_url": short_url}
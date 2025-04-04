from fastapi import FastAPI
from channelprocess.filter import get_channel_ids

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/scrape_channels")
async def scrape_channels():
    get_channel_ids()
    return {"message": "Channel scraping completed!"}

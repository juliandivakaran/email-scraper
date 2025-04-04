from pymongo import MongoClient
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "youtube_scraper"
COLLECTION_NAME = "channels"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
channels_collection = db[COLLECTION_NAME]
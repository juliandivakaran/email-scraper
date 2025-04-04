import time
from googleapiclient.discovery import build
from database.database import *
# YouTube API Key
API_KEY = "AIzaSyCEyfYafBqyJRnmlSPrdb_VSYMxH9mD21o"

# MongoDB Connection


# Keywords to search for
SEARCH_QUERIES = ["technology", "gaming", "fitness", "cooking", "science", "education", "music"]
MAX_RESULTS = 50  # Max allowed per request
TOTAL_IDS_NEEDED = 5000  # Goal

# Initialize YouTube API client
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_channel_ids(search_queries, max_results, total_needed):
    collected_count = 0
    request_count = 0

    for query in search_queries:
        print(f"Searching for: {query}")
        next_page_token = None

        while collected_count < total_needed and request_count < 100:
            request = youtube.search().list(
                q=query,
                type="channel",
                part="snippet",
                publishedAfter=start_date,
                publishedBefore=end_date,
                maxResults=max_results,
                pageToken=next_page_token
            )
            response = request.execute()
            request_count += 1

            for item in response.get("items", []):
                channel_id = item["snippet"]["channelId"]
                channel_name = item["snippet"]["title"]
                channel_created_date = item["snippet"]["publishedAt"]

                # Check if channel ID already exists in MongoDB
                if not channels_collection.find_one({"channel_id": channel_id}):
                    channel_data = {
                        "channel_id": channel_id,
                        "channel_name": channel_name,
                        "channel_created_date": channel_created_date
                    }
                    channels_collection.insert_one(channel_data)
                    collected_count += 1
                    print(f"Added: {channel_name} ({channel_id})")

            next_page_token = response.get("nextPageToken")
            if not next_page_token:
                break  # Stop if no more pages

            time.sleep(1)  # Respect API limits

        if collected_count >= total_needed:
            break  # Stop when enough IDs are collected

    print(f"Collected {collected_count} channel IDs.")
    return collected_count

start_date = '2024-01-01T00:00:00Z'
end_date = '2025-01-01T00:00:00Z'
# Run the function
get_channel_ids(SEARCH_QUERIES, MAX_RESULTS, TOTAL_IDS_NEEDED)

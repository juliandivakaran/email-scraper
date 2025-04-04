import database.database as db
import requests



def get_channel_ids_from_db():
    collection = db.db['channels']

    channel_ids = []

    try:
        channels = collection.find({},{'_id':0, 'channel_id':1})

        for channel in channels:
            print("https://www.youtube.com/channel/"+channel['channel_id'])

        print(f"Found {len(channel_ids)} channels")

    except Exception as e:
        print(e)

    return channel_ids


if __name__ == "__main__":
    get_channel_ids_from_db()
    #print(f"Found {len(channel_ids)} channels")